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

def updateAvgStart(event,time):
    """
    Calculates the average lateness/earliest that an event occurs.
    """
    event.startDiffs.append(time)
    event.avgStartDiffs = (sum(event.startDiffs))//len(event.startDiffs)

def checkEvent(event,dt,weekCheck):
    check = weekCheck.get("Did you " + event.name + " at " + datetime.time(dt.hour,dt.minute) + " on " + dt.weekday() + "? ")
    if check == "Yes":
        event.streak += 1
        return True
    elif check == "No":
        event.streak = 0
        return False

def checkTime(event,dt):
    check = input("How early(-) or late(+) did you " + event.name + "?")
    avgStartTime(event,check)

def loadSchedule():
    """
    Loads the schedule to the app.
    """
    try:
        sched = pickle.load("schedule.txt")
        return sched
    except:
        return 0

#def main():
    #load up last info
    #open pygame with last info
        #if no info, load empty schedule
    #load unchecked events (getTimeFrame(lastCheck,datetime.datetime.today()))
        #checkEvent(x[0],x[1]) for x in checkEvent
            #if checkEvent == True:
                #x[0].streak += 1
                #checkTime(x[0],x[1])
            #if checkEvent == False
                #x[0].streak = 0
    #sched.lastCheck = datetime.datetime.today()
    #if input event
        #add event
        #update schedule
    #if hover existing event
        #present event information
    #if  click existing event
        #present event editing
    #save all session info

# def main():
     #sched = loadSchedule()
     #if loadSchedule == 0:
         #pass
     #edit event
     #if doubleclick event:
         #open create event window
         #copy name, streak and lateness and input new event information (start,end,freq)
         #call editEvent([list of all events],newedited event) #will overwrite inputed changes