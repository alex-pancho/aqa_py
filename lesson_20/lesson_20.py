import time


my_time_01 = time.asctime((1980, 1, 2, 3, 4, 5, 6, 7, 8))
print(my_time_01)
my_real_time = time.asctime()
my_real_time_2 = time.asctime(time.localtime())
print("my time", my_real_time)
print(my_real_time == my_real_time_2)

nix_time = time.ctime(0)
print(nix_time)

nix_time_now = time.ctime(1686547846)
print(nix_time_now)

print(time.localtime())

print("*")

yant = time.strftime("Now year %Y %m day is %d time is: %H:%M",
                     time.localtime())
print(yant)

print(time.strptime("Sep 20, 2022", '%b %d, %Y'))
# print(time.strptime("Sep 20, 2022", '%b, %d, %Y'))  #  ValueError
print(time.strptime("13 12, 2022", '%d %m, %Y'))

incoming_date = "Aug 24, 1991"
dt_incoming_date = time.strptime(incoming_date, '%b %d, %Y')
print(time.strftime("OUR INDEPENDANCY DAY IS %Y month" +
                    " %m day is %d time is: %H:%M", dt_incoming_date))

print(time.time())
time.sleep(0.5)
print(time.time())
# The offset in seconds of the local time zone (without DST) from UTC
print(time.timezone)
