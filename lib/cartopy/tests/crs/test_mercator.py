# (C) British Crown Copyright 2013, Met Office
#
# This file is part of cartopy.
#
# cartopy is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cartopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cartopy.  If not, see <http://www.gnu.org/licenses/>.
import unittest

from numpy.testing import assert_almost_equal
from nose.tools import assert_equal, assert_true, assert_not_equal

import cartopy.crs as ccrs


def test_default():
    crs = ccrs.Mercator()

    assert_equal(crs.proj4_init, ('+ellps=WGS84 +proj=merc +lon_0=0.0 +k=1 '
                                  '+units=m +no_defs'))
    assert_almost_equal(crs.boundary.bounds,
                        [-20037508, -15496571, 20037508, 18764656], decimal=0)


def test_eccentric_globe():
    globe = ccrs.Globe(semimajor_axis=10000, semiminor_axis=5000,
                       ellipse=None)
    crs = ccrs.Mercator(globe=globe, min_latitude=-40, max_latitude=40)
    assert_equal(crs.proj4_init, ('+a=10000 +b=5000 +proj=merc +lon_0=0.0 '
                                  '+k=1 +units=m +no_defs'))

    assert_almost_equal(crs.boundary.bounds,
                        [-31415.93, -2190.5, 31415.93, 2190.5], decimal=2)

    assert_almost_equal(crs.x_limits, [-31415.93, 31415.93], decimal=2)
    assert_almost_equal(crs.y_limits, [-2190.5, 2190.5], decimal=2)


def test_equality():
    default = ccrs.Mercator()
    crs = ccrs.Mercator(min_latitude=0)
    crs2 = ccrs.Mercator(min_latitude=0)

    # Check the == and != operators.
    assert_equal(crs, crs2)
    assert_not_equal(crs, default)
    assert_true(crs != default)
    assert_not_equal(hash(crs), hash(default))
    assert_equal(hash(crs), hash(crs2))


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
