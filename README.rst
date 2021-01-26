.. README.rst for self-titled repo

Hi, I'm Derek
=============

Just an undergrad interested in financial math, machine learning, scientific +
distributed computing, and software development. Most of my work is in Python,
although recently I've been interested in building Python packages that are a
mixture of ``.py`` files and compiled shared objects. See the in-development
`c_npy_demo`__ repository that compares the performance of a pure Python
function using `numpy`__ against an essentially identical Python function
implemented in a C extension module using `NumPy C API`__. ``c_npy_demo`` also
includes a function timing C extension module that emulates `timeit`__ but
exposes a more convenient callable API for timing functions and gives slightly
more accurate [#]_ reported times.

.. __: https://github.com/phetdam/c_npy_demo

.. __: https://numpy.org/doc/stable/

.. __: https://numpy.org/doc/stable/reference/c-api/index.html

.. __: https://docs.python.org/3/library/timeit.html

.. [#] In the definition of ``timeit.Timer.timeit``, the timing of ``number``
   executions of the code snippet ``stmt`` is done by
   `timing the execution of a loop`__ that executes the snippet ``number``
   times. Looping in Python is slower than looping in C, so the average
   per-loop time reported by ``timeit`` is somewhat inflated. For example,
   the output of ``c_npy_demo.functimer.timeit_enh(max, (1, 2))`` is

   .. code:: text

      2000000 loops, best of 5: 104.3 nsec per loop

   The corresponding output from ``timeit.main(["max(1, 2)"])`` is

   .. code:: text

      1000000 loops, best of 5: 201 nsec per loop

   Of course, your mileage may vary, but repeating this experiment multiple
   times showed that the average per-loop time reported by
   ``c_npy_demo.functimer.timeit_enh`` was consistently lower than the average
   per-loop time reported by ``timeit.main``.

.. __: https://github.com/python/cpython/blob/master/Lib/timeit.py#L69


A sentiment
-----------

.. code:: c

   /* sentiment.c */

   #include <stdio.h>
   #include <stdlib.h>

   #define __boolean(x, y) !(((x) ^ (y)) && ((x) < (y)))

   char const *int2str(int i) {
     return !i ? "false" : "true";
   }

   int main(int argc, char const * const *argv) {
     printf("be %s to yourself\n", int2str(__boolean(5, 3)));
     return EXIT_SUCCESS;
   }

.. code:: bash

   gcc -o sentiment sentiment.c && ./sentiment