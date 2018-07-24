import math
import pickle
import datetime
import pygame
import random
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
background_color = (241,228,179)
listScreen = [SCREEN_WIDTH, SCREEN_HEIGHT]

# display screen
window = pygame.display.set_mode(listScreen)
window.fill(background_color)

# position
pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

# Colors
BLACK = (0, 0, 0)
WHEEL = (21,149,159)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (200,100,0) 
LINE = (19,48,70)
CORAL = (236,151,112)
 
# class event
# done

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
        self.inncolor = CORAL
        self.innRadius = (self.radius//3)*2
        self.tdplusfour = (pos[0], pos[1] + self.radius)
        self.tdplusfive = (pos[0] + self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        self.tdplussix = (pos[0] + self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.td = (pos[0] + self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.tdplusone = (pos[0] - self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.tdplustwo = (pos[0] - self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.tdplusthree = (pos[0] - self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        #self.font = pygame.font.Font("sunmed.ttf", 12)
        self.font = pygame.font.SysFont("Times", 14)
        self.bigFont = pygame.font.SysFont("Times", 24)
        # constants for plotting schedule
        self.eventRing = (self.radius+self.innRadius)//2
        self.eventRadius = 5
        self.active = []
        self.sched = Schedule([x[0] for x in week])
    
    def Color(self):
        """Assigns and keeps track of unique color per event"""
        lon = {}
        for i in range(len(self.loa)):
            if self.loa[i][0] not in lon:
                r = random.randint(10, 25)*10
                g = random.randint(10, 25)*10
                b = random.randint(10, 25)*10
                lon[self.loa[i][0]] = (r, g, b)
                self.loa[i].append((r,g,b))
            else:
                self.loa[i].append(lon[self.loa[i][0]])
                

    def Cartesian(self):
        # translated from time in day to x-y coordiantes
        # Given day and time, Returns Cartesian coordinates
        # use polar coordinates
        # theta = fraction of week * 2pi (in radians)
        
        # step 1: get polar
        self.eventRing = (self.radius+self.innRadius)//2
        self.today = datetime.datetime.today()
        self.start = week[0][1].weekday()
        for i in range(len(week)):
            self.loa += [[week[i][0] ,week[i][1].hour/24 + (week[i][1].weekday() - self.today.weekday())]]

        for i in range(len(self.loa)):
            self.loa[i][1] = self.loa[i][1]/7*(2*3.14)
        
        # translate polar to cartesian
        # x = r × cos( θ )
        # y = r × sin( θ )
        for i in range(len(self.loa)):
            self.loa[i][1] = (int(self.eventRing*math.cos(self.loa[i][1])),int(self.eventRing*math.sin(self.loa[i][1])))
        for i in range(len(self.loa)):
            self.loa[i][1] = ((pos[0]+self.loa[i][1][0]),(pos[1]+self.loa[i][1][1]))

    def draw(self):
        """Draws the days and events of this week"""
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
            eventColor = self.loa[i][2]
            if self.loa[i] == self.active:
                eventColor = (199, 64, 45)
            pygame.draw.circle(window, eventColor, self.loa[i][1] , self.eventRadius)
            name = self.font.render(self.loa[i][0].name, 10, self.loa[i][2])
            window.blit(name, (self.loa[i][1][0]-15, self.loa[i][1][1]+10))

        if len(self.active) != 0:
            centerTitle = self.bigFont.render(self.active[0].name, 10, BLUE)
            window.blit(centerTitle, (self.position[0]-(centerTitle.get_width()//2), self.position[1]))
            duration = "start: {} end: {}".format(self.active[0].start, self.active[0].end)
            frequency = "frequency: every {} days".format(self.active[0].freq)
            streak = "streak: every {} days".format(self.active[0].streak)
            lateness =  "average lateness: {}".format(self.active[0].avgStartDiff)
                     
            surfDuration = self.font.render(duration, 10, BLUE) 
            surfFrequency = self.font.render(frequency, 10, BLUE) 
            surfStreak = self.font.render(streak, 10, BLUE) 
            surfLateness = self.font.render(lateness, 10, BLUE) 

            window.blit(surfDuration, (self.position[0]-(surfDuration.get_width()//2), self.position[1]+30))
            window.blit(surfFrequency, (self.position[0]-(surfFrequency.get_width()//2), self.position[1]+50))
            window.blit(surfStreak, (self.position[0]-(surfStreak.get_width()//2), self.position[1]+70))
            window.blit(surfLateness, (self.position[0]-(surfLateness.get_width()//2), self.position[1]+90))
        
    def eventInfo(self, mousex, mousey):
        """When you click on a event (as represented by a circle)
        the event infor is listed, which is extracted from the object"""
        for i in range(len(self.loa)):    
            x = self.loa[i][1][0]
            y = self.loa[i][1][1] 
            d = math.sqrt((x-mousex)**2 + (y-mousey)**2)
            if d <= 5:
                self.active = self.loa[i]

    def getInput(self, prompt, pos):
        promptSurface = self.font.render(prompt,100,WHITE)
        window.blit(promptSurface, pos)
        pygame.display.flip()
        word=""
        wordSurface = self.font.render(word,100,BLACK)
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = False
                        self.draw()
                    else:
                        word+=chr(event.key)
                        wordSurface = self.font.render(word,100,BLACK)
                        window.blit(wordSurface, (pos[0], pos[1]+30))
                        pygame.display.flip()


        return word

    def getUncheckEvents(self):
        unchecked = self.sched.getTimeFrame(datetime.datetime(2018,7,16), datetime.datetime.today())
        print(unchecked)
        for x in unchecked:
            self.eventCheck(x[0],x[1])
    
    def eventCheck(self, event, dt):
        check = self.getInput("Did you " + event.name + " at " + str(datetime.time(dt.hour,dt.minute)) + " on " + str(dt.weekday()) + "? ", self.position)
        if check == "Yes":
            event.streak += 1
            return True
        elif check == "No":
            event.streak = 0
            return False
    


#self.active[0].freq

LoE = []
w = Week(LoE, pos)
w.Cartesian()
w.Color()

while True:
    w.draw()
    if datetime.datetime.today() != datetime.datetime(2018,7,16):
        w.getUncheckEvents()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            w.eventInfo(mousex, mousey)

    pygame.display.flip()
pygame.quit()
