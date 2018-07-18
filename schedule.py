import datetime
import eventgen

class Schedule(object):
    
    def __init__(self, name, start, freq):
        self.start = start
        self.month = start.month
        self.day = start.day
        self.year = start.year
        self.time = datetime.time(start.hour,start.minute)
        self.hour = start.hour
        self.minute = start.minute
        self.freq = freq
        self.name = name
        self.egInfo = eventgen.EventGen(name,start,freq)

    def createSchedule(self):
        """
        Writes a schedule for a given event into a text file
        called schedule.txt
        """
        f = open("schedule.txt", "w+")
        NthDays = self.egInfo.genSeq()
        daysList = self.egInfo.dayListStr()
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(daysList)):
            nth = datetime.timedelta(days=NthDays[x])
            newDate = start + nth
            schedDate = datetime.date(newDate.year,newDate.month,newDate.day)
            f.write('To {} on day {} on the date {} at {}.\r\n'.format(self.name,daysList[x],schedDate,self.time))
        f.close()
    
    def findCyclePoint(self):
        """
        Returns the most recent instantiation of an event.
        """
        nthNow = datetime.datetime.now() - self.start
        for x in range(len(self.egInfo.genSeq())):
            cyclePoint = self.egInfo.genSeq()[x]
            if nthNow < datetime.timedelta(days=self.freq):
                return 0
            elif nthNow < datetime.timedelta(days=cyclePoint):
                return x-1

    def createHistory(self):
        """
        Writes a history of instances of an event into a text 
        file called history.txt
        """
        f = open("history.txt", "w+")

    def resetSchedule(self):
        """
        Resets the schedule to have the start date be the next day
        (Used for when a cycle is broken)
        """

    def markEventDone(self):
        """
        Marks an event done for a certain date and time
        """

    def checkUndoneEvent(self):
        """
        Checks whether there are any events from the last check till now
        that have not been fulfilled
        """