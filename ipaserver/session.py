# Authors: John Dennis <jdennis@redhat.com>
#
# Copyright (C) 2011  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from ipalib.request import context
from ipalib.krb_utils import (
    krb5_parse_ccache,
)


def logout(ccache_name=None):
    if ccache_name is None:
        ccache_name = getattr(context, 'ccache_name', None)
    if ccache_name is not None:
        scheme, name = krb5_parse_ccache(ccache_name)
        if scheme == 'FILE':
            os.unlink(name)
    setattr(context, 'logout_cookie', '')
