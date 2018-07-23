import datetime
import eventgen
import schedule
import pickle
from operator import itemgetter

# open python
# get pickle file
# model schedule
# generate a list of events from model
# call a function to display the week of those events

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

def day(num):
    if num == 0:
        return 'Monday'
    elif num == 1:
        return 'Tuesday'
    elif num == 2:
        return 'Wednesday'
    elif num == 3:
        return 'Thursday'
    elif num == 4: 
        return 'Friday'
    elif num == 5:
        return 'Saturday'
    elif num == 6:
        return 'Sunday'

def overallStreak(allEvents):
    """
    Checks the streak of maintaining all event streaks
    """
    allStreaks = []
    for x in allEvents:
        allStreaks.append(x.streak)
    return min(allStreaks)

def avgStartTime(event,startTime):
    """
    Calculates the average lateness/earliest that an event occurs.
    """
    startDiff = event.datetime - startTime #needs to be datetime object!
    startDiffMins = startDiff.mins
    avg = (eventgen.avgStartDiff + startDiff)


def loadSchedule(self):
    """
    Loads the schedule to the app.
    """
    try:
        sched = pickle.load("schedule.txt")
        return sched
    except:
        return 0

# def main():
#     sched = loadSchedule()
#     if loadSchedule == 0:
#         pass
#     #edit event
#     if doubleclick event:
#         open create event window
#         copy name, streak and lateness and input new event information (start,end,freq)
#         call editEvent([list of all events],newedited event) #will overwrite inputed changes
    
# write pygame program that creates objects
# then picles them

# write program that reads pickle file and uses that to display the balls