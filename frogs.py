#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright notice
# ----------------
#
# Copyright (C) 2013-2014 Daniel Jung
# Contact: djungbremen@gmail.com
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
"""Frog definitions for this package."""
# 2014-06-09
from frog import Frog
import cheb


# cheb
optdoc = dict(n='set polynomial order', kind='set kind', symbol='set symbol')
f = Frog(inmap=dict(n='$0'),
    preproc=dict(n=int), outmap={0: '#@'},
    usage='cheb [options] ',
    optdoc=optdoc)
f(cheb.cheb)
