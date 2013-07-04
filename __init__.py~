#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implement a function that computes Chebychev polynomials iteratively.
Chebychev polynomials play a central role within the kernel polynomial
method [1].

[1] Weiße et al., Rev. Mod. Phys. 78, 275 (2006)

Author:  Daniel Jung, Jacobs University Bremen, Bremen, Germany.
Contact: d.jung@jacobs-university.de

To do:
--> let poly1d object have a display hook for pretty printing in IPython 
    notebook
"""
__created__ = '2013-07-04'
__modified__ = '2013-07-04'
import numpy

# if module "frog" exists, use it, otherwise, create a dummy decorator
try:
  from frog import Frog
except ImportError:
  class Frog(object):
    # dummy decorator
    def __init__(self, *args, **kwargs):
      pass
    def __call__(self, func):
      return func




optdoc = dict(n='set polynomial order', kind='set kind', symbol='set symbol')
@Frog(informat='ARGS', infiles=0, optdoc=optdoc)
def cheb(n=0, kind=1, symbol='x'):
  """Calculate Chebyshev polynomial of order "n" of first or second kind
  using iterative formula. Return numpy.poly1d object.

  Example:
  >>> import cheb
  >>> print cheb.cheb(2)
  >    2 
  > 2 x - 1
  >>> print cheb.cheb(n=3, kind=2, symbol='y')
  >    3
  > 8 y - 4 y"""
  # former tb.kpm._Cheb (developed 2011-09-14 until 2011-11-21)
  # former tb._Cheb (developed 2011-01-17 until 2011-04-08)
  __created__ = '2013-07-04'
  __modified__ = '2013-07-04'

  x = numpy.poly1d([1L, 0L])
  if kind == 1:
    # calculate Chebychev polynomial of first kind
    T = []
    T.append(numpy.poly1d([1.])) # T[0]
    T.append(x)                  # T[1]
    for m in xrange(1, n):
      T.append(2*x*T[m]-T[m-1])  # T[m+1]

    # set symbol
    for m in xrange(len(T)):
      T[m].__dict__['variable'] = symbol

    # return polynomial
    return T[n]

  elif kind == 2:
    # calculate Chebychev polynomial of second kind
    U = []
    U.append(numpy.poly1d([1L])) # U[0]
    U.append(2*x)                # U[1]
    for m in xrange(1, n):
      U.append(2*x*U[m]-U[m-1])  # U[m+1]

    # set symbol
    for m in xrange(len(U)):
      U[m].__dict__['variable'] = symbol

    # return polynomial
    return U[n]
  else:
    raise ValueError, 'kind must be 1 or 2'
