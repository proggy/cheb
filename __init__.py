#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright notice
# ----------------
#
# Copyright (C) 2013-2023 Daniel Jung
# Contact: proggy-contact@mailbox.org
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
#
"""Implement a function that computes Chebychev polynomials using a recursive
formula.


Background
----------

Chebychev polynomials play a central role within the kernel polynomial
method [1].

[1] Weiße et al., Rev. Mod. Phys. 78, 275 (2006)
"""
# To do:
# --> let poly1d object have a display hook for pretty printing in IPython
#     notebook
__version__ = '0.1.1'

import numpy

def cheb(n=0, kind=1, symbol='x'):
    """Calculate Chebyshev polynomial of order "n" of first or second kind
    using iterative formula. Return numpy.poly1d object.

    Example
    -------

    >>> import cheb
    >>> print(cheb.cheb(2))
       2
    2 x - 1
    >>> print(cheb.cheb(n=3, kind=2, symbol='y'))
       3
    8 y - 4 y
    """
    # former tb.kpm._Cheb (developed 2011-09-14 until 2011-11-21)
    # former tb._Cheb (developed 2011-01-17 until 2011-04-08)

    x = numpy.poly1d([1, 0])
    if kind == 1:
        # calculate Chebychev polynomial of first kind
        T = []
        T.append(numpy.poly1d([1.]))  # T[0]
        T.append(x)                  # T[1]
        for m in range(1, n):
            T.append(2*x*T[m]-T[m-1])  # T[m+1]

        # set symbol
        for m in range(len(T)):
            T[m].__dict__['variable'] = symbol

        # return polynomial
        return T[n]

    elif kind == 2:
        # calculate Chebychev polynomial of second kind
        U = []
        U.append(numpy.poly1d([1]))  # U[0]
        U.append(2*x)                # U[1]
        for m in range(1, n):
            U.append(2*x*U[m]-U[m-1])  # U[m+1]

        # set symbol
        for m in range(len(U)):
            U[m].__dict__['variable'] = symbol

        # return polynomial
        return U[n]
    else:
        raise ValueError('kind must be 1 or 2')


def __main__():
    import doctest
    doctest.testmod()
