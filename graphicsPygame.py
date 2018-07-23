import math
import pickle
import datetime
import pygame
import random
pygame.init()
pygame.font.init()

week = pickle.load(open("circadianInfo.txt","rb"))['SchedList']

# Global constants
# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
listScreen = [SCREEN_WIDTH, SCREEN_HEIGHT]

# display screen
window = pygame.display.set_mode(listScreen)

# position
pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (200,100,0) 
 
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
        self.color = BLUE
        self.radius = 300
        self.inncolor = GREEN
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
        # constants for plotting schedule
        self.eventRing = (self.radius+self.innRadius)//2
        self.eventRadius = 5
    
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
            self.loa += [[week[i][0].name ,week[i][1].hour/24 + (week[i][1].weekday() - self.today.weekday())]]

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
        pygame.draw.line(window, WHITE, self.position, self.tdplusfour)
        pygame.draw.line(window, WHITE, self.position, self.tdplusfive)
        pygame.draw.line(window, WHITE, self.position, self.tdplussix)
        pygame.draw.line(window, WHITE, self.position, self.td)
        pygame.draw.line(window, WHITE, self.position, self.tdplusone)
        pygame.draw.line(window, WHITE, self.position, self.tdplustwo)        
        pygame.draw.line(window, WHITE, self.position, self.tdplusthree)
        pygame.draw.circle(window, self.inncolor, self.position, self.innRadius)
        # draw events as dots
        
        for i in range(len(self.loa)):
            pygame.draw.circle(window, self.loa[i][2], self.loa[i][1] , self.eventRadius)
            name = self.font.render(self.loa[i][0], 0, self.loa[i][2])
            window.blit(name, (self.loa[i][1][0]-15, self.loa[i][1][1]+10))

# NEXT STEP: PLOT NAME WITH CORERCSPONDING COLOR

LoE = []
w = Week(LoE, pos)
w.Cartesian()
w.Color()
w.draw()


# plot lists of lists as dots
# assume, for now, that no two events occur at the same time

#  day class 

# Streak, global variable
 
# Go ahead and update the screen with what we've drawn.
pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
while True:
    pass

pygame.quit()
