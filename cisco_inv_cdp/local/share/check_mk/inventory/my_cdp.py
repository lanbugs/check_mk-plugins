#!/usr/bin/python

#
# Cisco CDP Inventory Extension - Shows CDP Neighbors of a Cisco device
# Use it on your own risk!
#
# Version 1.1
# Written 2017 - Maximilian Thoma
#
# Version 1.1 patch for Check_MK 1.5.x
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


def inv_cdp(info, params):

    node = inv_tree_list("networking.cdp:")
    
    local_if, remote_if = info

    if_dict={}
    
    for l_if_id,l_if_name in local_if:

        for  r_if_id, r_device, r_port, r_vlan in remote_if:
            if r_if_id.split(".")[:1][0] == l_if_id:
                node.append({

                "index"     : int(l_if_id),
                "l_if_name" : l_if_name,
                "r_device"  : r_device,
                "r_port"    : r_port,
                "r_vlan"    : int(r_vlan)

                })

inv_info["inv_cdp"] = {
                        "inv_function" : inv_cdp,
                        "snmp_info"    : [(".1.3.6.1.4.1.9.9.23.1.1.1.1", [OID_END,  # if string
                                                                          "6", # interface 
                                         ]),
                                          (".1.3.6.1.4.1.9.9.23.1.2.1.1", [OID_END,  # if string
                                                                          "6", # remote device name
                                                                          "7", # remote device port 
                                                                          "11", # vlan
                                         ]),
                                         ],
                  "snmp_scan_function" : lambda oid: oid(".1.3.6.1.4.1.9.9.23.*") != None,
                     }
