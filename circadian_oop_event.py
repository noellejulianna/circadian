class Event(object):
    """
    A user-defined data structure that stores and manipulates
    dates
    """
    def __init__(self, mo, dy, yr, freq, time):
        """
        Construct a Date with the given month, day, and year
        """
        self.month = mo
        self.day = dy
        self.year = yr
        self.freq = freq
        self.time = time
    
    def isLeapYear(self):
        """
        Every year divisible by 4 is a leap year.
        However, every year divisible by 100 is not a leap year.
        However, every year divisible by 400 is a leap year after all.
        """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False
    
    def isBefore(self, d2):
        """
        True if self is before d2, else False
        """
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.year == d2.year and self.month == d2.month:
            return True
        return False

    def __lt__(self, d2):
        """
        This is the less than replacement
        """
        return self.isBefore(d2)

    def __eq__(self,d2):
        """
        Returns True if self and d2
        represent the same date;
        False otherwise
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def diff(self,d2):
        """
        Takes one argument, d2, a Date object, and returns an integer
        representing the number of days between the calling object and d2
        """
        copyDate = self.copy()
        dayCount = 0
        while True:
            if copyDate.isAfter(d2) == True:
                copyDate.yesterday()
                dayCount += 1
            elif copyDate.isBefore(d2) == True:
                copyDate.tomorrow()
                dayCount -= 1
            elif copyDate == d2:
                break
        return dayCount

    def copy(self):
        """ 
        Returns a new object with the same month, day, year
        as the calling object (self).
        """
        d = Event(self.month, self.day, self.year)
        return d

    def tomorrow(self):
        """
        Changes the date stored in the calling object so that it
        respresents the next day
        """
        if self.isLeapYear(): fdays = 29
        else: fdays = 28

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.month += 1
            self.day = 1
            if self.month > 12:
                self.year += 1
                self.month = 1

    def addNDays(self, N):
        """
        Changes the calling object so that it represents
        N calendar days following the original date
        """
        for x in range(N):
            self.tomorrow()
    
    def isAfter(self, d2):
        """
        True if self is after d2, else False
        """
        if self.year > d2.year:
            return True
        elif self.month > d2.month and self.year == d2.year:
            return True
        elif self.day > d2.day and self.year == d2.year and self.month == d2.month:
            return True
        return False

    def dow(self):
        """
        Returns a string representing the day of the week
        of the date associated with calling Date object
        """
        Monday = Event(7,9,2018)
        if self.diff(Monday)%7 == 0:
            return 'Monday'
        elif self.diff(Monday)%7 == 1:
            return 'Tuesday'
        elif self.diff(Monday)%7 == 2:
            return 'Wednesday'
        elif self.diff(Monday)%7 == 3:
            return 'Thursday'
        elif self.diff(Monday)%7 == 4:
            return 'Friday'
        elif self.diff(Monday)%7 == 5:
            return 'Saturday'
        elif self.diff(Monday)%7 == 6: 
            return 'Sunday'