from datetime import datetime, date, time

class Event(object):

    def __init__(self, start, time, freq):
        """
        Construct a Event info with the given month, day, and year
        time of day, and frequency of the event
        """
        self.month = start.month
        self.day = dy
        self.year = yr
        self.time = time
        self.freq = freq

    def genSeq(self):
        """
        Generates a list of the nth day that the event will happen
        depending on its inputed frequency
        """
        NthDay = [0]
        for x in range(365/self.freq):
            NthDay += [NthDay[-1] + self.freq]
        return NthDay
        #Use the step argument of range

    def dayList(self):
        """
        Generates a list the NUMBERS OF THE DAY OF the week
        (i.e. Monday = 0, Tuesday = 1 etc)
        that the event will happen depending on its inputed 
        frequency
        """
        NthDay = self.genSeq()
        daysListNum = []
        daysList = []
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start = datetime.datetime(self.year,self.month,self.day)
        for x in range(len(NthDay)):
            nth = timedelta(days=NthDay[x])
            daysList += date(start+nth).weekday()
        for x in daysListNum

            






    



