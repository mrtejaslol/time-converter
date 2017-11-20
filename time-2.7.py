#!/usr/bin/python2.7
HourDifference=5 #modify according to your TimeZone
MinuteDifference=30 #modify according to your TimeZone

from datetime import datetime
now=datetime.now()
print "Local Time is: %s:%s:%s" %(now.hour,now.minute,now.second)

UnknownHour=now.hour-HourDifference
if UnknownHour<0:
    UnknownHour+=23
    """The number of hours is ones less since it is distributed into minutes below"""

UnknownMinute=now.minute-MinuteDifference
if UnknownMinute<0:
    gminute+=60
    """The number of minutes is 60 because i have ignored seconds"""

print "GMT is: %s:%s:%s" %(UnknownHour,UnknownMinute,now.second)
