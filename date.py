
import datetime

import pytz

#function to print current time and date

def currentdate ():
    now = datetime.datetime.now()
    print("The current date and time is", now)
currentdate()

#function to output all the available timezones of the world
def timezones ():
    zones = pytz.all_timezones
    print(zones)

timezones() 
