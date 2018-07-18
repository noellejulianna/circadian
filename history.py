import datetime
import eventgen
import schedule

class History(object):
    
    def __init__(self, name, start, end, freq):
        self.start = start
        self.end = end
        self.month = start.month
        self.day = start.day
        self.year = start.year
        self.time = datetime.time(start.hour,start.minute)
        self.hour = start.hour
        self.minute = start.minute
        self.freq = freq
        self.name = name
        self.egInfo = eventgen.EventGen(name,start,end,freq)
        self.sInfo = schedule.Schedule(name,start,end,freq)

    def __repr__(self):
        """
        Display a date in a nice format
        """
        s = "{:02}/{:02}/{:04}".format(self.month, self.day, self.year)
        return s
    
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
        mostRecent = self.findCyclePoint()
        f = open("history.txt", "w+")
        NthDays = list(self.egInfo.genSeq()[0:mostRecent+1])
        daysList = list(self.egInfo.dayListStr()[0:mostRecent+1])
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(daysList)):
            nth = datetime.timedelta(days=NthDays[x])
            newDate = start + nth
            schedDate = datetime.date(newDate.year,newDate.month,newDate.day)
            f.write('Supposed to {} on day {} on the date {} at {}.\r\n'.format(self.name,daysList[x],schedDate,self.time))
        f.close()

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