#!/usr/bin/env python

"""
"STATE": "ON",
"PROFILE": "Domain",
"CSTATE": "eingehend blockieren, ausgehend zulassen"
"""

register_check_parameters(
    subgroup_applications,
    "windows_firewall",
    "Windows Firewall Settings",

    Dictionary(
                elements = [
                ("STATE",
                TextAscii(title = _("State"), default_value="ON"),
                ),
                ("PROFILE",
                TextAscii(title = _("Profile"), default_value="Domain"),
                ),
                ("CSTATE",
                TextAscii(title = _("Connection State"), default_value="eingehend blockieren, ausgehend zulassen"),
                ),
                   ],
                  optional_keys = None,
                ),
    None,
   'dict',
)


