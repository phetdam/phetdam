.. README.rst for self-titled repo

Hi, I'm Derek
=============

Recent graduate broadly interested in optimization, machine learning, and
scientific computing. Most of my work is in Python, although recently I've been
interested in building Python C extensions to speed up computations, using the
`Python C API`__ and `NumPy C API`__ to work with Python objects on the C
level. For example, the `numpy-lapacke-demo`__ package implements linear
regression and Newton's method with diagonal Hessian modification in C
extensions, performing the computations using `CBLAS`__\ /\ `LAPACKE`__
routines operating directly on NumPy array memory. All public and private
methods are also rigorously unit tested using `pytest`__.

.. __: https://docs.python.org/3/c-api/index.html

.. __: https://numpy.org/doc/stable/reference/c-api/index.html

.. __: https://github.com/phetdam/numpy-lapacke-demo

.. __: http://www.netlib.org/blas/

.. __: https://www.netlib.org/lapack/lapacke.html

.. __: https://docs.pytest.org/en/stable/

For fun, here's a toy norm-constrained convex optimization problem and a plot
of its solution against the objective's minimum. The code used to solve the
problem and generate the plot can be found in `my profile repository`__.

.. __: https://github.com/phetdam/phetdam

.. image:: https://raw.githubusercontent.com/phetdam/phetdam/master/
   contours.png
   :alt: contours.png