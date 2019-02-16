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


def inv_lldp(info, params):

    node = inv_tree("networking.lldp:")

    local_if, remote_if = info

    r_if_dict={}

    for r_if_id, r_hostname, r_ifname in remote_if:
        x, r_if_index, y = r_if_id.split(".")
        r_if_dict[r_if_index]={"hostname":r_hostname,"ifname":r_ifname}


    for l_id, l_long, l_short in local_if:
        if l_id in r_if_dict:

            node.append({

            "index"      : int(l_id),
            "l_ifname"   : l_long,
            "r_ifname"   : r_if_dict[l_id]["ifname"],
            "r_hostname" : r_if_dict[l_id]["hostname"],

            })

inv_info["inv_lldp"] = {
                        "inv_function" : inv_lldp,
                        "snmp_info"    : [(".1.0.8802.1.1.2.1.3.7.1", [OID_END, # lldp_ifindex
                                                                      "4", # local if long
                                                                      "3" # local if short
                                         ]),
                                          (".1.0.8802.1.1.2.1.4.1.1", [OID_END, # if string
                                                                      "9", # hostname
                                                                      "8", # remote if name
                                         ]),
                                         ],
                  "snmp_scan_function" : lambda oid: oid(".1.0.8802.1.*") != None,
                      }
