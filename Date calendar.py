from datetime import datetime
import calendar
d=datetime.now()
print(calendar.month(2021,5))
print(calendar.month(d.year,d.month))
print(calendar.monthrange(2021,5))
print(calendar.monthrange(2021,6))
print(calendar.monthrange(2021,7))
# to get weekday of first day of the month and number of days in month
#https://www.w3resource.com/python/module/calendar/monthrange.php