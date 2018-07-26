import datetime
import eventgen
import schedule
import pickle
from operator import itemgetter

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

def wname(n):
    """
    Converts datetime.weekday() output into the string of the weekday
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[n]

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