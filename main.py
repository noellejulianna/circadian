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

def readDate(dt):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
    dayOfWeek = days[dt.weekday()]
    month = months[dt.month-1]
    return '{} {} {}'.format(dayOfWeek,month,str(dt.day))

def overallStreak(allEvents):
    """
    Checks the streak of maintaining all event streaks
    """
    allStreaks = []
    for x in allEvents:
        allStreaks.append(x.streak)
    return min(allStreaks)

def loadSchedule():
    """
    Loads the schedule to the app.
    """
    try:
        sched = pickle.load("schedule.txt")
        return sched
    except:
        return 0

def removeDups(lst):
    """
    Removes duplicate events in a schedule list
    """
    if len(lst) <= 1:
        return lst
    else:
        if lst[0] in lst[1:]:
            return removeDups(lst[1:])
        else:
            return [lst[0]] + removeDups(lst[1:])

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