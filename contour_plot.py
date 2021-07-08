__doc__ = """Generate the contour plot shown in the README.rst.

Level sets of the objective, the unconstrained solution, and the constrained
solution are plotted using matplotlib. Solution obtained using trust-constr.

Function minimized is a convex bivariate quadratic function. The constraint is
an L1 norm constraint requiring the solution to be at most unit norm, although
the threshold value can be adjusted by the user.

Script should be run from the terminal. Pass --help for usage.

.. codeauthor:: Derek Huang <djh458@stern.nyu.edu>
"""

# pylint: disable=import-error
import argparse
from functools import partial
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from scipy.optimize import LinearConstraint, minimize
import sys


_HELP_MIN_POINT = """\
Minimizer of the unconstrained problem. Should be in the format x1,x2. \
"""
_HELP_THRESHOLD = "Maximum value the 1-norm of the solution can take."
_HELP_FIG_HEIGHT = """\
Height of the resulting figure in inches. The width of the figure is given \
by (2 * x1 + 1.2 * THRESHOLD) * FIG_HEIGHT / (2 * x2 + 1.2 * THRESHOLD).\
"""
_HELP_N_SAMPLES = """\
Number of samples to use along each plotting axis when making the contour \
plot. Increasing the value improves the smoothness of the contours.\
"""
_HELP_FILE_NAME = "Name of file to save the matplotlib-generated figure to."


def p_float(x):
    """Attempts to convert x to positive float.

    Parameters
    ----------
    x : object

    Returns
    -------
    float
    """
    x = float(x)
    if x <= 0:
        raise ValueError("x cannot be converted to positive float")
    return x


def p_int(x):
    """Attempts to convert x to positive int.

    Parameters
    ----------
    x : object

    Returns
    -------
    float
    """
    x = int(x)
    if x < 1:
        raise ValueError("x cannot be converted to positive float")
    return x


def css2tuple(s):
    """Converts a comma-separated string of values to a tuple of floats.

    Parameters
    ----------
    s : str
        String where values are separated by commas

    Returns
    -------
    tuple
        Resulting tuple with values converted to floats
    """
    return tuple(map(float, s.split(",")))


def exec_main(
    min_point=(3, 2), threshold=1., fig_height=3.,
    n_samples=100, file_name="contours.png"
):
    """Main executing method of the that drives all the computations.

    Does the "real" work in the script, i.e. computation and plotting.

    Parameters
    ----------
    min_point : tuple, default=(3, 2)
        Minimizer of the unconstrained problem.
    threshold : float, default=1.
        Maximum 1-norm of the constrained solution.
    fig_height : float, default=3.
        Height of the resulting figure. The actual (width, height) of the
        figure is (2 * x1 + 1.2 * threshold, 2 * x2 + 1.2 * threshold) scaled
        so that the height is fig_height.
    n_samples : int, default=100
        Number of sample points to use along either axis when drawing the
        contour plots. Increase the number for smoother contours.
    file_name : str, default="contours.png"
        Name of the file the figure will be saved to.

    Returns
    -------
    None
    """
    # get separated x1, x2 + convert to numpy array
    x1, x2 = min_point
    min_point = np.array(min_point)
    print(f"unconstrained solution: {min_point}")
    # function, gradient, and hessian
    quad_func = lambda x: (
        0.5 * (x[0] - x1) ** 2 + (x[1] - x2) ** 2 +
        0.5 * (x[0] - x1) * (x[1] - x2)
    )
    quad_grad = lambda x: (
        np.array(
            [
                (x[0] - x1 + 0.5 * (x[1] - x2)),
                2 * (x[1] - x2) + 0.5 * (x[0] - x1)
            ]
        )
    )
    quad_hess = lambda x: np.array([[1, 0.5], [0.5, 2]])
    # L1 norm constraint on solution, rewritten as linear constraints
    norm_constraint = [
        LinearConstraint(np.ones(2), -np.inf, threshold),
        LinearConstraint(-np.ones(2), -np.inf, threshold),
        LinearConstraint([[-1, 0], [0, 1]], -np.inf, threshold),
        LinearConstraint([[1, 0], [0, -1]], -np.inf, threshold)
    ]
    # compute solution to constrained problem
    x_hat = minimize(
        quad_func, np.zeros(2), method="trust-constr", jac=quad_grad,
        hess=quad_hess, constraints=norm_constraint
    ).x
    print(f"constrained solution:   {x_hat}")
    # x, y coordinate grids to plot objective contours over
    x_grid, y_grid = np.meshgrid(
        np.linspace(-1.2 * threshold, 2.3 * x1, num=n_samples),
        np.linspace(-1.2 * threshold, 2.3 * x2, num=n_samples)
    )
    # compute objective values on grid for contour plot
    f_vals = np.empty(x_grid.shape)
    for i in range(f_vals.shape[0]):
        for j in range(f_vals.shape[1]):
            f_vals[i, j] = quad_func([x_grid[i, j], y_grid[i, j]])
    ## plotting of contours and constraints ##
    # compute width and height scaled so height = fig_height
    fwidth = (
        (2.3 * x1 + 1.3 * threshold) * fig_height / (2.3 * x2 + 1.3 * threshold)
    )
    fheight = fig_height
    # create figure using fwidth, fheight
    fig, ax = plt.subplots(figsize=(fwidth, fheight))
    # plot norm constraint (plot above contours). save the returned Patch so
    # we can set its label for the legend later.
    norm_patch = ax.add_patch(
        Polygon(
            np.array(
                [
                    [-threshold, 0], [0, threshold],
                    [threshold, 0], [0, -threshold]
                ]
            ),
            alpha=0.4, color="blue", zorder=10
        )
    )
    # plot the optimal unconstrained and constrained points (plot on top)
    ax.scatter(x1, x2, marker="d", c="orange", zorder=20)
    ax.scatter(x_hat[0], x_hat[1], marker="x", c="red", zorder=20)
    levels = np.linspace(
        0, quad_func(x_hat), num=int(0.6 * ax.get_xticks().size)
    )
    # plot area covered by the objective contours. we save the QuadContourSet
    # for when we need to set the labels in the legend later.
    contourf_set = ax.contourf(
        x_grid, y_grid, f_vals, levels=levels, alpha=0.15, colors="red"
    )
    # plot contours of the function itself
    ax.contour(x_grid, y_grid, f_vals, levels=levels)
    # set labels for function highlight area under the contours and the norm
    # constraint. to get the color entry in the legend, we make an empty
    # Patch using a Polygon that is a single point with the same color.
    dummy_patch = ax.add_patch(
        Polygon(
            np.zeros(4).reshape(2, 2),
            # get_facecolor returns list of RGBA, so we drop a dimension
            color=contourf_set.collections[0].get_facecolor().squeeze()
        )
    )
    # order of setting labels matters, so set dummy_patch label first with the
    # objective before setting the norm constraint label. equalize axes scaling
    ax.set_aspect("equal")
    ax.legend(
        [dummy_patch, norm_patch],
        [
            r"$ \frac{1}{2}(x_1 - 3)^2 + (x_2 - 2)^2 + "
            r"\frac{1}{2}(x_1 - 3)(x_2 - 2) $",
            r"$ |x_1| + |x_2| \leq 1 $"
        ]
    )
    # make tight and save
    fig.tight_layout()
    fig.savefig(file_name)
    print(f"plot saved to {file_name}")


def main(args=None):
    """Main method of the script.

    Doesn't do much besides parse arguments and serve as the entry point.

    Parameters
    ----------
    args : list, default=None
        List of string arguments to parse. If None, arguments passed on the
        command line when the script is run are parsed.

    Returns
    -------
    0 on success.
    """
    # add main parser
    arp = argparse.ArgumentParser(
        formatter_class=partial(
            argparse.ArgumentDefaultsHelpFormatter, width=80
        )
    )
    # add arguments
    arp.add_argument(
        "-m", "--min-point", type=css2tuple, default="3,2", help=_HELP_MIN_POINT
    )
    arp.add_argument(
        "-t", "--threshold", type=p_float, default=1., help=_HELP_THRESHOLD
    )
    arp.add_argument(
        "-H", "--fig-height", type=p_float, default=3., help=_HELP_FIG_HEIGHT
    )
    arp.add_argument(
        "-n", "--n-samples", type=p_int, default=100, help=_HELP_N_SAMPLES
    )
    arp.add_argument(
        "-f", "--file-name", type=str,
        default="contours.png", help=_HELP_FILE_NAME
    )
    # parse arguments
    args = arp.parse_args(args=args)
    # run main execution method
    exec_main(
        min_point=args.min_point, threshold=args.threshold,
        fig_height=args.fig_height, n_samples=args.n_samples,
        file_name=args.file_name
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())