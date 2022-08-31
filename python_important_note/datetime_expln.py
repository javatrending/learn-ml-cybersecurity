from datetime import datetime

# to get the current date/time which is the timestamp
timestamp_now = datetime.now()
print(" This result is the current date and time: ", timestamp_now)

# get the difference between two timestamps
time_difference = datetime(2022, 8, 14) - datetime(2015, 2, 13, 0, 59)
print(" Time difference (days in past 2015): ", time_difference.days, " days")
print(" Time difference (seconds in past 2015): ", time_difference.seconds, " second")
print(" Time difference (year in past 2015): ", round(time_difference.days/365, 1), " year")

print(50*"=")

# creating date objects
## The datetime() class requires three parameters to create a date: year, month, day. And optional parameters such as hour, minute, second

x = datetime(2020, 5, 17)
print("Date objecst: ", x)
print("Name of the month: ", x.strftime("%B"))



# Resources: https://www.w3schools.com/python/python_datetime.asp