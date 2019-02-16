#!/usr/bin/python


#
# LLDP Inventory Extension - Shows LLDP Neighbors of a network device
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

    ".networking.lldp:"                              : { "title" : _("LLDP Informations"), "render" : render_inv_dicttable,  "view" : "invlldp_of_host", "keyorder": 
["index","l_ifname","r_ifname","r_hostname"] },
    ".networking.lldp:*.index"                   : { "title" : _("Index") },
    ".networking.lldp:*.l_ifname"                   : { "title" : _("Local Interface") },
    ".networking.lldp:*.r_ifname"               : { "title" : _("Remote Interface") },
    ".networking.lldp:*.r_hostname"              : { "title" : _("Remote Host Name") },
})

declare_invtable_view("invlldp", ".networking.lldp:", _("LLDP Interface"), _("LLDP Interfaces"))
