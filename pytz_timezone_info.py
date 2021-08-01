# -*- coding: utf-8 -*-
"""
timezones with pytz module
print all the country names and current local time for 
each timezone in the country
"""
import pytz
import datetime


for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo timezone defined")


