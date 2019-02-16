#!/usr/bin/python

#
# Cisco CDP Inventory Extension - Shows CDP Neighbors of a Cisco device
# Use it on your own risk!
#
# Version 1.0
# Written 2017 - Maximilian Thoma
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program; if not,
# write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110, USA
#


inventory_displayhints.update({
    ".networking.cdp:"              : { "title"    : _("CDP Informations"),
                                        "render"   : render_inv_dicttable,
                                        "view"     : "invcdp_of_host",
                                        "keyorder" : ["index", "l_if_name", "r_device", "r_port", "r_vlan"] },
    ".networking.cdp:*.index"       : { "title" : _("Index") },
    ".networking.cdp:*.l_if_name"   : { "title" : _("Local Interface") },
    ".networking.cdp:*.r_device"    : { "title" : _("Remote Device Name") },
    ".networking.cdp:*.r_port"      : { "title" : _("Remote Port") },
    ".networking.cdp:*.r_vlan"      : { "title" : _("VLAN") },
})

declare_invtable_view("invcdp", ".networking.cdp:", _("CDP Interface"), _("CDP Interfaces"))

