# vim: set fileencoding=utf-8 :
#
# (C) 2012 Intel Corporation <markus.lehtonen@linux.intel.com>
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, please see
#    <http://www.gnu.org/licenses/>
"""Temporary directory handling"""

import os
import tempfile

from gbp.errors import GbpError

def mkdtemp(dir, **kwargs):
    """Create temporary directory"""
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError as (dummy_e, msg):
        raise GbpError, "Unable to create dir %s (%s)" % (dir, msg)

    try:
        return os.path.abspath(tempfile.mkdtemp(dir=dir, **kwargs))
    except OSError as (dummy_e, msg):
        raise GbpError, "Unable to create tmpdir under %s (%s)" % (dir, msg)

# vim:et:ts=4:sw=4:et:sts=4:ai:set list listchars=tab\:»·,trail\:·:

