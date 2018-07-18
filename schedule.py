import datetime
import eventgen

class Schedule(object):
    
    def __init__(self, event, start=None, end=None):
        if start == None:
            self.start = event.start
        else:
            self.start = start
        if end == None:
            self.end = event.end
        else:
            self.end = end
        self.month = start.month
        self.day = start.day
        self.year = start.year
        self.egInfo = [event]

    def createSchedule(self):
        """
        Writes a schedule for a given event into a text file
        called schedule.txt
        """
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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
                else:
                    events += [x.name,fullDate]
        events.sort()
        with open("schedule.txt", "w+") as f:
            for b in events:
                f.write('To {} on day {} on the date {} at {}.\r\n'.format(b.name,days[b.weekday()],b.date(),b.time()))