.. README.rst for self-titled repo

Hi, I'm Derek
=============

Recent graduate broadly interested in optimization, machine learning, and
scientific computing. Most of my work is in Python, although recently I've been
interested in building Python packages that mix Python and C code. See the
`c_npy_demo`__ repository that compares the performance of a pure Python
function using `numpy`__ against an essentially identical Python C extension
module function using the `NumPy C API`__.

.. __: https://github.com/phetdam/c_npy_demo

.. __: https://numpy.org/doc/stable/

.. __: https://numpy.org/doc/stable/reference/c-api/index.html


A sentiment
-----------

.. code:: c

   /* sentiment.c */

   #include <stdio.h>
   #include <stdlib.h>

   #define xor_boolean(x, y) !(((x) ^ (y)) && ((x) < (y)))

   char const *int2str(int i) {
     return !i ? "false" : "true";
   }

   int main(int argc, char const * const *argv) {
     printf("be %s to yourself\n", int2str(xor_boolean(5, 3)));
     return EXIT_SUCCESS;
   }

.. code:: bash

   gcc -o sentiment sentiment.c && ./sentiment

.. image:: https://raw.githubusercontent.com/phetdam/phetdam/master/contours.png
   :alt: contours.png