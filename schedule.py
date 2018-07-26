import datetime
import eventgen
import pickle
import main
import random
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
        self.eventColors = [(218,65,103),(180,99,73),(165,180,82),(178,154,69),(15,113,115),(84,69,127),(119,29,55),(51,24,50),(111,29,27)]
        self.egInfo = []
        if type(event) == list:
            for x in event:
                self.addEvent(x)
        else:
            self.addEvent(event)
        self.schedList = []
        self.lastCheck = datetime.datetime.today()

    def createSchedule(self):
        """
        Writes a schedule for a given event into a text file
        called schedule.txt
        """
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
                    break
                elif fullDate < self.start:
                    continue
                else:
                    events += [[x,fullDate]]
        eventsFinal = sorted(events, key=itemgetter(1))
        for b in eventsFinal:
            self.schedList.append([b[0],b[1]])
        self.schedList = main.removeDups(self.schedList)
        return self.schedList
    
    def getWeek(self):
        """
        Loads a list of events for the current day to the next week
        """
        today = datetime.datetime.today()
        self.start = datetime.datetime(today.year,today.month,today.day)
        self.end = self.start + datetime.timedelta(days=7)
        self.schedList = []
        self.createSchedule()
        return self.schedList

    def getTimeFrame(self, start, end):
        """
        Loads a lit of events for a fixed timeframe
        """
        self.start = start
        self.end = end
        self.schedList = []
        self.createSchedule()
        return self.schedList

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
        self.schedList = []
        self.schedList = pickle.load(open("circadianInfo.txt", "rb"))['SchedList']

    def editEvent(self, newEvent):
        self.egInfo.append(newEvent)
        self.createSchedule()

    def addEvent(self, newEvent):
        """
        Adds a new event object to the schedule.
        """
        if newEvent.color == ():
            doneColors = [x.color for x in self.egInfo]
            freeColors = [x for x in self.eventColors if x not in doneColors]
            if len(freeColors) != 0:
                newEvent.color = random.choice(freeColors)
            else:
                newEvent.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
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
    