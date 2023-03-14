
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

#function to get current date and time based on time zone

def current_time_in_nairobi ():
    Nairobi_TZ = pytz.timezone("Africa/Nairobi")
    NairobiTime = datetime.datetime.now(Nairobi_TZ)
    currentTimeInNairobi = NairobiTime.strftime("%Y:%b:%a:%d:%H:%M:%S:%p")
    print(currentTimeInNairobi)

current_time_in_nairobi()
