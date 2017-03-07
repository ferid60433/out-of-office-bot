# -*- coding: utf-8 -*-
import arrow
import datetime
from meya import Component


class CheckIfOpen(Component):

    def start(self):
        # now in current timezone
        now = arrow.now().to("US/Eastern")

        # open 9:30 - 18:00, Monday - Friday
        if 0 <= now.weekday() <= 4:
            start = datetime.time(9, 30)
            end = datetime.time(18, 0)

            if (start <= now.time() <= end):
                # open! (during work hours)
                action = "open"
            else:
                # outside of work hours
                action = "closed"

        else:
            # weekend
            action = "closed"

        return self.respond(action=action)
