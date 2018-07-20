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

def editEvent(allEvents,newEvent):
    """
    Edits event
    """
    for x in allEvents:
        if x.name == newEvent.name:
            if x.start != newEvent.start:
                x.start = newEvent.start
            if x.end != newEvent.end:
                x.end = newEvent.end
            if x.freq != newEvent.freq:
                x.freq = newEvent.freq

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
    #edit event
    if doubleclick event:
        open create event window
        copy name, streak and lateness and input new event information (start,end,freq)
        call editEvent([list of all events],newedited event) #will overwrite inputed changes
    
write pygame program that creates objects
then picles them

write program that reads pickle file and uses that to display the balls