import datetime
import eventgen
import pickle
from operator import itemgetter

class Main(object):
    
    def __init__(self):
        try:
            self.schedule = pickle.load("schedule.txt")
        except:
            self.schedule = self.makeSchedule()

    def makeSchedule(self):
        eventName = input("What good habit would you like to start? ")
        eventStart
        eventEnd
        eventFreq
        