import datetime
import eventgen
import pickle
import main
from operator import itemgetter

class Schedule(object):
    
    def __init__(self, event, start=None, end=None):
        if start == None:
            start = event[0].start
            for x in event[1:]:
                if x.start < start:
                    start = x.start
            self.start = start
        else:
            self.start = start
        if end == None:
            end = event[0].end
            for x in event[1:]:
                if x.end > end:
                    end = x.end
            self.end = end
        else:
            self.end = end
        self.month = start.month
        self.day = start.day
        self.year = start.year
        self.egInfo = event
        self.schedList = []
        self.lastCheck = datetime.datetime.today()

    def createSchedule(self):
        """
        Writes a schedule for a given event into a text file
        called schedule.txt
        """
        #days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        events = []
        for x in self.egInfo:
            if x.start > self.end:
                continue
            NthDays = x.genSeq()
            for i in NthDays:
                nth = datetime.timedelta(days=i)
                newDate = x.start + nth
                fullDate = datetime.datetime(newDate.year,newDate.month,newDate.day,x.hour,x.minute)
                if fullDate > self.end:
                    continue
                elif fullDate < self.start:
                    continue
                else:
                    events += [[x,fullDate]]
        eventsFinal = sorted(events, key=itemgetter(1))
        for b in eventsFinal:
            self.schedList.append([b[0],b[1]])
            #self.schedList.append('To {} on day {} on the date {} at {}.\r\n'.format(b[0],days[b[1].weekday()],b[1].date(),b[1].time()))
        return self.schedList
    
    def getWeek(self):
        """
        Loads a list of events for the current day to the next week
        """
        today = datetime.datetime.today()
        self.start = datetime.datetime(today.year,today.month,today.day)
        self.end = self.start + datetime.timedelta(days=7)
        self.createSchedule()
        return self.schedList

    def getTimeFrame(self, start, end):
        """
        Loads a lit of events for a fixed timeframe
        """
        self.start = start
        self.end = end
        self.createSchedule()
        return self.schedList

    # def checkStreaks(self):
    #     """
    #     Maintains the streak count for every event and updates the last check 
    #     """
    #     if 
    #     uncheckedEvents = self.getTimeFrame(self.lastCheck,datetime.datetime.today())
    #     for x in uncheckedEvents:
    #         check = input("Did you " + x[0].name + " at " + datetime.time(x[1].hour,x[1].minute) + " on " + x[1].weekday() + "? ")
    #         if check == "Yes":
    #             x.streak += 1
    #         elif check == "No":
    #             x.streak = 0
    #     self.lastCheck = datetime.datetime.today()

    def saveSchedule(self):
        """
        Pickles the schedule.
        """
        circadianInfo = {'SchedList': self.schedList,"LastCheck": self.lastCheck}
        with open("circadianInfo.txt", "wb") as f:
            pickle.dump(circadianInfo, f)

    def loadSchedule(self):
        """
        Loads the schedule to the app.
        """
        self.schedList = pickle.load("circadianInfo.txt", "rb")

    def addEvent(self, newEvent):
        """
        Adds a new event object to the schedule.
        """
        self.egInfo.append(newEvent)
        
    def findCyclePoint(self):
        """
        Returns the most recent instantiation of an event.
        """
        eventPoints = []
        for anEvent in self.egInfo:
            cycleNow = 0
            nthNow = datetime.datetime.now() - anEvent.start
            for anOccurence in range(len(anEvent.genSeq())):
                cyclePoint = anEvent.genSeq()[anOccurence]
                lastPoint = anEvent.genSeq()[anOccurence-1]
                if nthNow < datetime.timedelta(days=anEvent.freq):
                    cycleNow = 0
                    break
                elif nthNow == datetime.timedelta(days=cyclePoint):
                    cycleNow = anOccurence
                    break
                elif datetime.timedelta(days=lastPoint) < nthNow < datetime.timedelta(days=cyclePoint):
                    cycleNow = anOccurence-1
                    break
            eventPoints.append([anEvent.name,cycleNow])
        return eventPoints
    
    # def checkUndoneEvent(self):
    #     """
    #     Checks whether there are any events from the last check till now
    #     that have not been fulfilled
    #     """
    #     f = open("history.txt")
    #     eventLines = f.read()
    #     f.close()
    #     LoE = eventLines.split('\n')
    #     for x in range(len(LoE)):

    # def markEventDone(self):
    #     """
    #     Marks an event done for a certain date and time
    #     """
    #     done = input("")

    # def resetSchedule(self):
    #     """
    #     Resets the schedule to have the start date be the next day
    #     (Used for when a cycle is broken)
    #     """

#design schedule for start date to any end date
#schedule should be able to list multiple events 
#store as event objects and sort them

#Statistics I want to keep
    
    