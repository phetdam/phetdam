.. README.rst for self-titled repo

Hi, I'm Derek
=============

Recent graduate [#]_ broadly interested in optimization, machine learning, and
scientific computing, mainly using Python, C++, and C. In particular, most of
my personal and professional work has been done in Python, C++17, and C++20.

For fun, here's a toy norm-constrained convex optimization problem and a plot
of its solution against the objective's minimum. The Python script used to
solve the problem and generate the plot can be found in
`my profile repository`__.

.. __: https://github.com/phetdam/phetdam

.. image:: https://raw.githubusercontent.com/phetdam/phetdam/master/contours.png
   :alt: contours.png

Selected projects
-----------------

npyglue_
   C++ project aimed at simplifying creation of NumPy arrays from C++ objects
   providing the backing memory. Supported backing objects include STL vectors,
   Armadillo_ and Eigen_ matrices, and `PyTorch C++`_ CPU/GPU tensors.
   Integration layers include the Python C/C++ API layer and SWIG_. Unit and
   integration tests in C++/Python are all orchestrated with CTest_.

.. _Armadillo: https://arma.sourceforge.net/

.. _Eigen: https://libeigen.gitlab.io/

.. _PyTorch C++: https://docs.pytorch.org/cppdocs/

.. _SWIG: https://www.swig.org/

.. _CTest: https://cmake.org/cmake/help/latest/manual/ctest.1.html

numpy-lapacke-demo_
   Python C extension implementations of linear regression using QR/SVD and
   Newton's method with diagonal Hessian modification using the `Python C API`_
   and `NumPy C API`_ to work with Python objects on the C level. Computations
   are done using `CBLAS`_\ /\ `LAPACKE`_ routines operating directly on NumPy
   array memory. All public and private methods are rigorously unit tested
   using `pytest`_.

.. _Python C API: https://docs.python.org/3/c-api/index.html

.. _NumPy C API: https://numpy.org/doc/stable/reference/c-api/index.html

.. _npyglue: https://github.com/phetdam/npyglue

.. _numpy-lapacke-demo: https://github.com/phetdam/numpy-lapacke-demo

.. _CBLAS: http://www.netlib.org/blas/

.. _LAPACKE: https://www.netlib.org/lapack/lapacke.html

.. _pytest: https://docs.pytest.org/en/stable/

.. [#] NYU Stern May 2021, BS in finance and joint BA in math/computer science.
