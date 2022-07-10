from datetime import time, date

meeting_start = time(hour=11, minute=15, second=0)
print(meeting_start)
meeting_end = time(hour=12, minute=30)
print(meeting_end)

# below will return a TypeError
# meeting_time = meeting_end - meeting_start
# print(meeting_time)
