import calendar

yr = int(input("Enter the year="))
if calendar.isleap(yr):
  print(yr, "is a leap uear")
else:
  print(yr, "is not a leap year")