.. README.rst for self-titled repo

Hi, I'm Derek
=============

Recent graduate [#]_ broadly interested in optimization, machine learning, and
scientific computing, mainly using Python, C++, and C. Most of my personal and
professional work has been in Python, although lately I find myself using C++,
namely C++17, more and more.

For fun, here's a toy norm-constrained convex optimization problem and a plot
of its solution against the objective's minimum. The code used to solve the
problem and generate the plot can be found in `my profile repository`__.

.. __: https://github.com/phetdam/phetdam

.. image:: https://raw.githubusercontent.com/phetdam/phetdam/master/
   contours.png
   :alt: contours.png

Recent activity
---------------

numpy-lapacke-demo_
   Python C extension implementations of linear regression using QR/SVD and
   Newton's method with diagonal Hessian modification using the `Python C API`_
   and `NumPy C API`_ to work with Python objects on the C level. Computations
   are done using `CBLAS`_\ /\ `LAPACKE`_ routines operating directly on NumPy
   array memory. All public and private methods are rigorously unit tested
   using `pytest`_.

.. _Python C API: https://docs.python.org/3/c-api/index.html

.. _NumPy C API: https://numpy.org/doc/stable/reference/c-api/index.html

.. _numpy-lapacke-demo: https://github.com/phetdam/numpy-lapacke-demo

.. _CBLAS: http://www.netlib.org/blas/

.. _LAPACKE: https://www.netlib.org/lapack/lapacke.html

.. _pytest: https://docs.pytest.org/en/stable/

.. [#] NYU Stern May 2021, BS in finance and joint BA in math/computer science.
