import math
import pickle
import datetime
import pygame
import random
import main
from schedule import Schedule
pygame.init()
pygame.font.init()

unpickled = pickle.load(open("circadianInfo.txt","rb"))
week = unpickled['SchedList']
lastCheck = unpickled['LastCheck']

# Global constants 
# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
background_color = (172,160,185)
listScreen = [SCREEN_WIDTH, SCREEN_HEIGHT]

# display screen
window = pygame.display.set_mode(listScreen)
window.fill(background_color)

# position
pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

# Colors
BLACK = (0, 0, 0)
WHEEL = (234, 235, 242)
WHITE = (234, 235, 242)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (200,100,0) 
LINE = (112,132,164)
INNER = (112,132,164)
DAYS = (57,79,99)
INPUT = (79,73,85)

# week class
# keeps track of days and events in week and displays
class Week(object):
    def __init__(self, LoE, pos):
        """Constructor, Pass a LoE,
        returns an object of type week"""
        self.loa = []
        self.events = LoE
        self.position = pos
        self.color = WHEEL
        self.radius = 300
        self.inncolor = INNER
        self.innRadius = (self.radius//3)*2
        self.tdplusfour = (pos[0], pos[1] + self.radius)
        self.tdplusfive = (pos[0] + self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        self.tdplussix = (pos[0] + self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.td = (pos[0] + self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.tdplusone = (pos[0] - self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.tdplustwo = (pos[0] - self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.tdplusthree = (pos[0] - self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        #self.font = pygame.font.Font("sunmed.ttf", 12)
        self.inputFont = pygame.font.Font("RalewayInput.ttf", 14)
        self.font = pygame.font.Font("Raleway.ttf", 14)
        self.bigFont = pygame.font.Font("Roboto.ttf", 24)
        # constants for plotting schedule
        self.eventRing = (self.radius+self.innRadius)//2
        self.eventRadius = 5
        self.active = []
        self.sched = Schedule([x[0] for x in week])
        self.sched.getWeek()
                
    def Cartesian(self):
        # translated from time in day to x-y coordiantes
        # Given day and time, Returns Cartesian coordinates
        # use polar coordinates
        # theta = fraction of week * 2pi (in radians)
        
        # step 1: get polar
        self.eventRing = (self.radius+self.innRadius)//2
        self.today = datetime.datetime.today()
        self.start = self.sched.schedList[0][1].weekday()
        for i in range(len(self.sched.schedList)):
            self.loa += [[self.sched.schedList[i][0],self.sched.schedList[i][1].hour/24 + (self.sched.schedList[i][1].weekday() - self.today.weekday()-2.25), self.sched.schedList[i][1]]]
        for i in range(len(self.loa)):
            try:
                self.loa[i][1] = self.loa[i][1]/7*(2*3.14)
            except:
                pass
        
        # translate polar to cartesian
        # x = r × cos( θ )
        # y = r × sin( θ )
        for i in range(len(self.loa)):
            try:
                self.loa[i][1] = (pos[0]+int(self.eventRing*math.cos(self.loa[i][1])),pos[1]+int(self.eventRing*math.sin(self.loa[i][1])))
            except:
                pass

    def draw(self):
        """Draws the days and events of this week"""
        window.fill(background_color)
        pygame.draw.circle(window, self.color, self.position, self.radius)
        pygame.draw.line(window, LINE, self.position, self.tdplusfour)
        pygame.draw.line(window, LINE, self.position, self.tdplusfive)
        pygame.draw.line(window, LINE, self.position, self.tdplussix)
        pygame.draw.line(window, LINE, self.position, self.td)
        pygame.draw.line(window, LINE, self.position, self.tdplusone)
        pygame.draw.line(window, LINE, self.position, self.tdplustwo)        
        pygame.draw.line(window, LINE, self.position, self.tdplusthree)
        pygame.draw.circle(window, self.inncolor, self.position, self.innRadius)
        
        for i in range(len(self.loa)):
            eventColor = self.loa[i][0].color
            if self.loa[i] == self.active:
                eventColor = (199, 64, 45)
            pygame.draw.circle(window, eventColor, self.loa[i][1] , self.eventRadius)
            name = self.font.render(self.loa[i][0].name, 10, self.loa[i][0].color)
            window.blit(name, (self.loa[i][1][0]-25, self.loa[i][1][1]+5))

        if len(self.active) != 0:
            centerTitle = self.bigFont.render(self.active[0].name, 40, WHITE)
            window.blit(centerTitle, (self.position[0]-(centerTitle.get_width()//2), self.position[1]-80))
            activityInfo = "{} at {}".format(main.readDate(self.active[2]), self.active[0].time)
            mainDetails = self.bigFont.render(activityInfo,40, WHITE)
            window.blit(mainDetails, (self.position[0]-(mainDetails.get_width()//2), self.position[1]-50))
            start = "You started {} on {}, {} ".format(self.active[0].name,main.readDate(self.active[0].start), self.active[0].start.year)
            end = "You plan to stop {} on {}, {} ".format(self.active[0].name,main.readDate(self.active[0].end), self.active[0].end.year)
            frequency = "You do this every {} days".format(self.active[0].freq)
            streak = "You havent missed {} for {} days".format(self.active[0].name,self.active[0].streak)
            lateness =  "On average, you do this {} minutes off".format(self.active[0].avgStartDiff)
                     
            surfStart = self.font.render(start, 40, WHITE) 
            surfEnd = self.font.render(end, 40, WHITE)
            surfFrequency = self.font.render(frequency, 40, WHITE) 
            surfStreak = self.font.render(streak, 40, WHITE) 
            surfLateness = self.font.render(lateness, 40, WHITE) 

            window.blit(surfStart, (self.position[0]-(surfStart.get_width()//2), self.position[1]))
            window.blit(surfEnd, (self.position[0]-(surfEnd.get_width()//2), self.position[1]+20))
            window.blit(surfFrequency, (self.position[0]-(surfFrequency.get_width()//2), self.position[1]+40))
            window.blit(surfStreak, (self.position[0]-(surfStreak.get_width()//2), self.position[1]+60))
            window.blit(surfLateness, (self.position[0]-(surfLateness.get_width()//2), self.position[1]+80))

        # display overall streak
        streakCount = main.overallStreak([x[0] for x in self.loa])
        stringStreak = str(streakCount)
        streak =  self.bigFont.render(stringStreak + " days", 40, WHITE)
        window.blit(streak, ((self.position[0]-streak.get_width()//2), (self.position[1]-1.25*self.radius)))

             
        # weekday helper function
        def wname(n):
            if n == 0:
                return "Monday"
            elif n == 1:
                return "Tuesday"
            elif n == 2:
                return "Wednesday"
            elif n == 3:
                return "Thursday"
            elif n == 4:
                return "Friday"
            elif n == 5:
                return "Saturday"
            elif n == 6:
                return "Sunday"

        # label days on pie, rotate days for today to  be at the top,
        # a for loop could also be used
        current = datetime.datetime.today()
        today = self.bigFont.render(wname(current.weekday()), 100, DAYS)
        # rotate day name to be tangent to pie
        # rotate (surface, angle)
        rtd = pygame.transform.rotate(today, 0)
        # draws our day name surface
        window.blit(rtd, (self.td[0] +85, self.td[1]- 60))

        # today plus one    
        todayplus1 = self.bigFont.render(wname((current+datetime.timedelta(days=1)).weekday()), 100, DAYS)
        rtdplus1 = pygame.transform.rotate(todayplus1, 305)
        window.blit(rtdplus1, (self.tdplusone[0] + 90, self.tdplusone[1]+35))

        # today plus two           
        todayplus2 = self.bigFont.render(wname((current+datetime.timedelta(days=2)).weekday()), 100, DAYS)
        rtdplus2 = pygame.transform.rotate(todayplus2, 260)
        window.blit(rtdplus2, (self.tdplustwo[0], self.tdplustwo[1] + 90))

        # today plus threes
        todayplus3 = self.bigFont.render(wname((current+datetime.timedelta(days=3)).weekday()), 100, DAYS)
        rtdplus3 = pygame.transform.rotate(todayplus3, 210)
        window.blit(rtdplus3, (self.tdplusthree[0] - 130, self.tdplusthree[1] + 55))

        # today plus four
        todayplus4 = self.bigFont.render(wname((current+datetime.timedelta(days=4)).weekday()), 100, DAYS)
        rtdplus4 = pygame.transform.rotate(todayplus4, 160)
        window.blit(rtdplus4, (self.tdplusfour[0]- 180, self.tdplusfour[1] - 40))

        # today plus five
        todayplus5 = self.bigFont.render(wname((current+datetime.timedelta(days=5)).weekday()), 100, DAYS)
        rtdplus5 = pygame.transform.rotate(todayplus5, 105)
        window.blit(rtdplus5, (self.tdplusfive[0] - 100, self.tdplusfive[1] - 155))

        # today plus six
        todayplus6 = self.bigFont.render(wname((current+datetime.timedelta(days=6)).weekday()), 100, DAYS)
        rtdplus6 = pygame.transform.rotate(todayplus6, 60)
        window.blit(rtdplus6, (self.tdplusfive[0] - 75, self.tdplussix[1] - 155))

    def eventInfo(self, mousex, mousey):
        """When you hover on a event (as represented by a circle)
        the event infor is listed, which is extracted from the object"""
        for i in range(len(self.loa)):    
            x = self.loa[i][1][0]
            y = self.loa[i][1][1] 
            d = math.sqrt((x-mousex)**2 + (y-mousey)**2)
            if d <= 5:
                self.active = self.loa[i]

    def eventEdit(self, mousex, mousey):
        """When you hover on a event (as represented by a circle)
        the event infor is listed, which is extracted from the object"""
        for i in range(len(self.loa)):    
            x = self.loa[i][1][0]
            y = self.loa[i][1][1] 
            d = math.sqrt((x-mousex)**2 + (y-mousey)**2)
            if d <= 5:
                self.active = []
                self.draw()
                self.getNewEventInfo(self.loa[i][0])

    def getInput(self, prompt, pos):
        promptSurface = self.font.render(prompt,100,WHITE)
        window.blit(promptSurface, (pos[0]-promptSurface.get_width()//2, pos[1]))
        pygame.display.flip()
        word=""
        wordSurface = self.inputFont.render(word,100,INPUT)
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = False
                        self.draw()
                    else:
                        word+=chr(event.key)
                        promptSurface = self.font.render(prompt,100,WHITE)
                        window.blit(promptSurface, (pos[0]-promptSurface.get_width()//2, pos[1]))
                        wordSurface = self.inputFont.render(word,100,INPUT)
                        window.blit(wordSurface, (pos[0]-wordSurface.get_width()//2, pos[1]+30))
                        pygame.display.flip()
                        self.draw()
        return word

    def getUncheckEvents(self):
        unchecked = self.sched.getTimeFrame(datetime.datetime(2018,7,23), datetime.datetime.today())
        for x in unchecked:
            self.eventCheck(x[0],x[1])
    
    def eventCheck(self, event, dt):
        check = self.getInput("Did you " + event.name + " at " + str(datetime.time(dt.hour,dt.minute)) + " on " + main.readDate(dt) + "? ",pos)
        if "y" in check:
            event.streak += 1
            self.getTimeChange(event)
            return True
        else:
            event.streak = 0
            return False
    
    def getTimeChange(self, event):
        timeChange = self.getInput("How many minutes -/+" + str(event.time) + " did you do " + event.name + " ? ", pos)
        event.startDiffs.append(int(timeChange))
        event.avgStartDiff = (sum(event.startDiffs))//len(event.startDiffs)
        self.sched.getWeek()
        self.sched.saveSchedule()
    
    def removeEditedEvent(self, event):
        self.sched.schedList = [x for x in self.sched.schedList if event != x[0]]

    def getNewEventInfo(self,event):
        self.startChange(event)
        self.endChange(event)
        self.freqChange(event)
        self.removeEditedEvent(event)
        self.sched.addEvent(event)
        self.sched.getWeek()
        self.sched.saveSchedule()

    def startChange(self, event):
        newStart = self.getInput("How many days from now do you want to restart your cycle? ", self.position)
        if newStart != 'x':
            event.start = datetime.datetime.today() + datetime.timedelta(days=int(newStart))

    def endChange(self, event):
        newEnd = self.getInput("How days do you want to do this for? ", self.position)
        if newEnd != 'x':
            event.end = event.start + datetime.timedelta(days=int(newEnd))

    def freqChange(self, event):
        newFreq = self.getInput("New frequency: ", self.position)
        if newFreq != 'x':
            event.freq = int(newFreq)

LoE = []
w = Week(LoE, pos)
w.Cartesian()

testDay = datetime.datetime(2018,7,20)

while True:
    w.draw()
    if datetime.date.today() != testDay:
        w.getUncheckEvents()
        testDay = datetime.date.today()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            w.eventInfo(mousex, mousey)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            w.eventEdit(mousex, mousey)
            w = Week([], pos)
            w.sched.loadSchedule()
            w.Cartesian()
    pygame.display.flip()
pygame.quit()


