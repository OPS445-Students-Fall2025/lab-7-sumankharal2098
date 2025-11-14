#!/usr/bin/env python3
# Student ID:sashank

from lab7c import *

t1 = Time(8,0,0)
t2 = Time(8,55,0)
t3 = Time(9,50,0)
td = Time(0,50,0)

tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
change_time(t3, 1800)

print(format_time(t1), "+", format_time(td), "-->", format_time(tsum1))
print(format_time(t2), "+", format_time(td), "-->", format_time(tsum2))
print("09:50:00 + 1800 sec -->", format_time(t3))
