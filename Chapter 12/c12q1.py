import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.setfirstweekday(calendar.THURSDAY) # for the part b
cal.pryear(2012)                   # What happens here

#so, it prints out a calendar? Mondo Cool

x=calendar.isleap(2012)
print(x)