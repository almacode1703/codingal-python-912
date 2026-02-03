import datetime  
    
# using now() to get current time  
current_time = datetime.datetime.now()  
    
# Printing value of now.  
print ("Time now at greenwich meridian is : ", end = "")   
print (current_time)

# print calendar of year 2021
import calendar
print("\n", calendar.calendar(2021))

# display current month calendar
now = datetime.datetime.now()
print("\nCurrent month calendar:")
print(calendar.month(now.year, now.month))