import datetime

class Event(object):

    def __init__(self, name, start, freq):
        """
        Construct a Event info with the given month, day, and year
        time of day, and frequency of the event
        """
        self.start = start
        self.month = start.month
        self.day = start.day
        self.year = start.year
        self.time = start.hour,start.minute
        self.hour = start.hour
        self.minute = start.minute
        self.freq = freq
        self.name = name

    def genSeq(self):
        """
        Generates a list of the nth day that the event will happen
        depending on its inputed frequency
        """
        NthDay = list(range(0,366,self.freq))
        return NthDay

    def dayListNums(self):
        """
        Generates a list the NUMBERS OF THE DAY OF the week
        (i.e. Monday = 0, Tuesday = 1, etc.)
        that the event will happen depending on its inputed 
        frequency.
        """
        NthDay = self.genSeq()
        daysList = []
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(NthDay)):
            nth = datetime.timedelta(days=NthDay[x])
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
    
    def yearRoutine(self):
        """
        Generates a list of the days, dates, and times that the event will
        happen.
        """
        NthDay = self.genSeq()
        daysList = self.dayListStr()
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(daysList)):
            nth = datetime.timedelta(days=NthDay[x])
            newDate = start + nth
            print("I will", self.name, "on", daysList[x], datetime.datetime(newDate.year,newDate.month,newDate.day), "at", self.hour, ":", self.minute)

            






    



