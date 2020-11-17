#!/usr/bin/python
#
# Title:       Moderate Security Announcement for python3 SUSE-SU-2020:3262-1
# Description: Security fixes for SUSE Linux Enterprise 12 SP0
# Source:      Security Announcement Parser v1.5.2
# Modified:    2020 Nov 16
#
##############################################################################
# Copyright (C) 2020 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "python3"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-November/007738.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'python3'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:3262-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libpython3_4m1_0': '3.4.10-25.55.1',
			'libpython3_4m1_0-32bit': '3.4.10-25.55.1',
			'libpython3_4m1_0-debuginfo': '3.4.10-25.55.1',
			'libpython3_4m1_0-debuginfo-32bit': '3.4.10-25.55.1',
			'python3': '3.4.10-25.55.1',
			'python3-base': '3.4.10-25.55.1',
			'python3-base-debuginfo': '3.4.10-25.55.1',
			'python3-base-debuginfo-32bit': '3.4.10-25.55.1',
			'python3-base-debugsource': '3.4.10-25.55.1',
			'python3-curses': '3.4.10-25.55.1',
			'python3-curses-debuginfo': '3.4.10-25.55.1',
			'python3-dbm': '3.4.10-25.55.1',
			'python3-dbm-debuginfo': '3.4.10-25.55.1',
			'python3-debuginfo': '3.4.10-25.55.1',
			'python3-debugsource': '3.4.10-25.55.1',
			'python3-devel': '3.4.10-25.55.1',
			'python3-devel-debuginfo': '3.4.10-25.55.1',
			'python3-tk': '3.4.10-25.55.1',
			'python3-tk-debuginfo': '3.4.10-25.55.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

