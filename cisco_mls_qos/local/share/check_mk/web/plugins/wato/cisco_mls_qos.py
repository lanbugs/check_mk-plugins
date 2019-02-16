#!/usr/bin/env python


register_check_parameters(
    subgroup_networking,
    "cisco_mls_qos",
    "Cisco MLS QoS Queues and Threshold",

    valuespec = ListOf(
      Tuple(
          show_titles = True,
          orientation = "vertical",
          elements = [
             Integer(
                 title = _("Queue"),
             ),
             Integer(
                 title = _("Threshold"),
             ),
             Float(
                 title = _("Warning drop Packets per Second"),
             ),
             Float(
                 title = _("Critical drop Packets per Second"),
             ),
             Float(
                 title = _("Warning enqueued Packets per Second"),
             ),
             Float(
                 title = _("Critical enqueued Packets per Second"),
             ),
          ]
      ),
      add_label = _("Add pattern"),
    ),
    itemspec=TextAscii(
        title = _("Index of the Port"),
    ),
    match_type = 'all',

)

