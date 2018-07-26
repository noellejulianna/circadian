import datetime

class EventGen(object):

    def __init__(self, name, start, end, freq):
        """
        Construct a Event info with the given month, day, and year
        time of day, and frequency of the event
        """
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
        self.streak = 0
        self.startDiffs = []
        self.avgStartDiff = 0
        self.color = ()


    def __eq__(self, event):
        if self.name == event.name and self.freq == event.freq and self.start == event.start:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name) ^ hash(self.freq) ^ hash(self.start)

    def genSeq(self):
        """
        Generates a list of the nth day that the event will happen
        depending on its inputed frequency
        """
        totalDaysTD = self.end - self.start
        totalDaysINT = int(totalDaysTD/datetime.timedelta(days=1))
        NthDays = list(range(0,totalDaysINT+1,self.freq))
        return NthDays

    def dayListNums(self):
        """
        Generates a list the NUMBERS OF THE DAY OF the week
        (i.e. Monday = 0, Tuesday = 1, etc.)
        that the event will happen depending on its inputed 
        frequency.
        """
        NthDays = self.genSeq()
        daysList = []
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(NthDays)):
            nth = datetime.timedelta(days=NthDays[x])
            newDate = start + nth
            daysList += [datetime.date(newDate.year,newDate.month,newDate.day).weekday()]
        return daysList

    def dayListStr(self):
        """
        Generates a list of the days of the week that the event will happen
        depending on its inputed frequency.
        """
        daysList = self.dayListNums()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for x in range(len(daysList)):
            daysList[x] = days[daysList[x]]
        return daysList


    
    
            






    



