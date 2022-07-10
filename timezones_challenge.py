import datetime as dt
import zoneinfo

# times in following places
# London, Paris, Hong Kong, Kolkata, Nairobi, Sydney, New York

# first create a tuple of timezone keys
# check date_time_examples for time zones
timezones = (
    'Europe/London',
    'Europe/Paris',
    'Asia/Hong_Kong',
    'Asia/Kolkata',
    'Africa/Nairobi',
    'Australia/Sydney',
    'America/New_York',
    'America/Los_Angeles'
)

# crate a utc now object
utc_now = dt.datetime.now(dt.timezone.utc)
print(f'Current UTC time is  {utc_now}')

local_now = dt.datetime.now()
print(f'Current Local time is {local_now}')

# loop over the timezones tuple and get current time for different tz
print('Showing Times in different timezones')
for _tz in timezones:
    tz_info = zoneinfo.ZoneInfo(_tz)

    # this converts the utc time to required timezone
    # dt_now = utc_now.astimezone(tz=tz_info)

    # this creates the current time in the required timezone
    # dt_now = dt.datetime.now(tz=tz_info)

    # converts the local time in required timezones
    dt_now = local_now.astimezone(tz_info)

    # replace 0 will remove the specified element from the object, e.g microsecond removed
    # we can add any other value to replace to change that element
    # print(f'Current Time in {_tz.split("/")[-1]} is {dt_now.replace(microsecond=0)}')

    # another way to do the above is strftime
    print(f'Current Time in {_tz.split("/")[-1]} is {dt_now.strftime("%Y-%m-%d %H:%M:%S %z %Z")}')


# testing replace function
# e.g. if month is replaced with another month which has less days
# will return a Value Error
# creating a date in January i.e. month=1
dt_time = dt.datetime(year=2022, month=1, day=31)
# now replace the month with 2 i.e. Feb
# this should return : ValueError: day is out of range for month
feb_dt = dt_time.replace(month=2)
print(feb_dt)
