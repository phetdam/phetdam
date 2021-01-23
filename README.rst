.. README.rst for self-titled repo

Hi, I'm Derek
=============

Just an undergrad interested in financial math, machine learning, scientific +
distributed computing, and software development. Most of my work is in Python,
although recently I've been interested in building Python packages that are a
mixture of ``.py`` files and compiled shared objects. See the in-development
`c_npy_demo`__ repository for an evolving example of how to combine pure Python
with a C extension module, access to the `NumPy C API`__, and a standalone
shared object wrapped with ctypes__.

.. __: https://github.com/phetdam/c_npy_demo

.. __: https://numpy.org/doc/stable/reference/c-api/index.html

.. __: https://docs.python.org/3/library/ctypes.html

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