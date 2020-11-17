#!/usr/bin/python
#
# Title:       Moderate Security Announcement for systemd SUSE-SU-2020:1842-1
# Description: Security fixes for SUSE Linux Enterprise 12 SP4
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
META_COMPONENT = "systemd"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-July/007072.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'systemd'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:1842-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'libsystemd0': '228-150.86.3',
			'libsystemd0-32bit': '228-150.86.3',
			'libsystemd0-debuginfo': '228-150.86.3',
			'libsystemd0-debuginfo-32bit': '228-150.86.3',
			'libudev-devel': '228-150.86.3',
			'libudev1': '228-150.86.3',
			'libudev1-32bit': '228-150.86.3',
			'libudev1-debuginfo': '228-150.86.3',
			'libudev1-debuginfo-32bit': '228-150.86.3',
			'systemd': '228-150.86.3',
			'systemd-32bit': '228-150.86.3',
			'systemd-bash-completion': '228-150.86.3',
			'systemd-debuginfo': '228-150.86.3',
			'systemd-debuginfo-32bit': '228-150.86.3',
			'systemd-debugsource': '228-150.86.3',
			'systemd-devel': '228-150.86.3',
			'systemd-sysvinit': '228-150.86.3',
			'udev': '228-150.86.3',
			'udev-debuginfo': '228-150.86.3',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

