import datetime as dt
from datetime import datetime, timezone
import zoneinfo

today = dt.datetime.today()
print(today)

now = datetime.now()
print(now)

# prefer now() over today() 
# as now also accepts a tzinfo parameter
# which can get the current time in that time zone

utc_now = datetime.utcnow()
print(utc_now)

# aware time = means the object contains timezone information
# naive = means object does not contain timezone information

utc_now_ = datetime.now(timezone.utc)
print(utc_now_)
local_now = utc_now_.astimezone()
print(local_now)
# there is no space in the tz info name - so underscores
ny_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now_.astimezone(tz=ny_tz)
print(ny_now)

print()
print('TimeZone keys')
print('-'*25)
for key in sorted(zoneinfo.available_timezones()):
    print(key)
