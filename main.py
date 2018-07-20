import datetime
import eventgen
import schedule
import pickle
from operator import itemgetter

open python
get pickle file
model schedule
generate a list of events from model
call a function to display the week of those events

def loadSchedule(self):
    """
    Loads the schedule to the app.
    """
    try:
        sched = pickle.load("schedule.txt")
        return sched
    except:
        return 0

def main():
    sched = loadSchedule()
    if loadSchedule == 0:
        pass
    
write pygame program that creates objects
then picles them

write program that reads pickle file and uses that to display the balls