# -*- coding: utf-8 -*-
"""
obspy.neic CWB Query module for ObsPy
=====================================
The obspy.neic package contains a client for the NEIC CWB Query server. A
public server is at 137.227.224.97 (cwbpub.cr.usgs.gov) on port 2061.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import absolute_import
from __future__ import unicode_literals

from .client import Client  # NOQA


if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
