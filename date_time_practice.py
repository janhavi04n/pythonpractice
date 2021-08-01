# -*- coding: utf-8 -*-
"""
practice for date, datetime, calendar modules
"""
import time
import datetime
import pytz
# from time import perf_counter as pc
# from time import monotonic as mo
# from time import time as tm
# from time import process_time as pt


# prints the UTC time - epoch time
print(time.gmtime(0))

# prints local time
print(time.localtime())

# prints num of seconds since epoch i.e. 1 Jan 1970
print(time.time())

# prints timezone information - tuple with (timezone, dst name)
print(time.tzname)
print("I am in '{0}' timezone".format(time.tzname[0]))

# if daylight saving is not in effect then it returns 0
print(time.daylight)

# strftime returns a string representation of a time in a particular format
print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))

# datetime functions
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.today())


    

    
