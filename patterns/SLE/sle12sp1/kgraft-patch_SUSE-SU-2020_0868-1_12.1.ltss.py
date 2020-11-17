#!/usr/bin/python
#
# Title:       Important Security Announcement for kgraft-patch SUSE-SU-2020:0868-1
# Description: Security fixes for SUSE Linux Kernel Live Patch 12 SP1 LTSS
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
META_COMPONENT = "kgraft-patch"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-April/006672.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'kgraft-patch'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0868-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'kgraft-patch-3_12_74-60_64_110-default': '9-2.1',
			'kgraft-patch-3_12_74-60_64_110-xen': '9-2.1',
			'kgraft-patch-3_12_74-60_64_115-default': '8-2.1',
			'kgraft-patch-3_12_74-60_64_115-xen': '8-2.1',
			'kgraft-patch-3_12_74-60_64_118-default': '6-2.1',
			'kgraft-patch-3_12_74-60_64_118-xen': '6-2.1',
			'kgraft-patch-3_12_74-60_64_121-default': '6-2.1',
			'kgraft-patch-3_12_74-60_64_121-xen': '6-2.1',
			'kgraft-patch-3_12_74-60_64_124-default': '4-2.1',
			'kgraft-patch-3_12_74-60_64_124-xen': '4-2.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

