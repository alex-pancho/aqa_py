import time
from datetime import datetime
from datetime import timedelta
# import datetime

# print(datetime.datetime.fromtimestamp(1686590971))
print(datetime.fromtimestamp(1686590971))
print(type(datetime.fromtimestamp(1686590971)))
# nix_time_now = time.strftime("%Y-%m-%d %H:%M:%s", time.ctime(1686590971))
# print(nix_time_now)
# print(type(nix_time_now)) ## ОБЄКТИ РІНОГО ТИПУ !!!!
d = datetime.today()
print(d)
print(d.ctime() == time.ctime(time.time()))  # TRUE
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())

incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date+timedelta(hours=16, minutes=25))
