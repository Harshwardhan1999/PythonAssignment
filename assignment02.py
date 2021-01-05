#question2
#Write a Python program to calculate the number of days between two dates.
#Sample dates : (20200702), (20200711)

from datetime import datetime, timedelta

date1= "20200702"
date2= "20200711"

first_date= datetime(year=int(date1[0:4]), month=int(date1[4:6]), day=int(date1[6:8]))
last_date = datetime(year=int(date2[0:4]), month=int(date2[4:6]), day=int(date2[6:8]))

no_of_days = last_date - first_date
print(no_of_days.days)