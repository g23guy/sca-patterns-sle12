#!/usr/bin/python

# Title:       Additional Support Contract: PostgreSQL Database
# Description: 1.4.3.1 Software Requiring Specific Contracts
# Modified:    2014 Oct 20
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
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
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Technology"
META_COMPONENT = "Support"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Note"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Note=https://www.suse.com/releasenotes/x86_64/SUSE-SLES/12/#Intro.Support.Techpreviews|META_LINK_Support=https://www.suse.com/releasenotes/x86_64/SUSE-SLES/12/#fate-316990|META_LINK_Fate=https://fate.suse.com/316990"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def anyPackageFound(PACKAGES):
	for PACKAGE_NAME in PACKAGES:
		if ( SUSE.packageInstalled(PACKAGE_NAME) ):
			return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

PACKAGES = ('postgresql93', 'postgresql93-server')
if( anyPackageFound(PACKAGES) ):
	Core.updateStatus(Core.WARN, "PostgreSQL Requires a Specific Support Contract")
else:
	Core.updateStatus(Core.ERROR, "Packages not found requiring additional support: " + str(PACKAGES))

Core.printPatternResults()


