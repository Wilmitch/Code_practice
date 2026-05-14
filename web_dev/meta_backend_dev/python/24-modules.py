#!/usr/bin/python3
import sys
locations = sys.path
print(locations)
for i in locations:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2036)
isleapyear = calendar.isleap(2032)
print(leapdays)
print(isleapyear)
