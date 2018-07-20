import math
import pickle
import datetime
import pygame
pygame.init()

week = pickle.load(open("schedule.txt","rb"))

# Global constants
# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
listScreen = [SCREEN_WIDTH, SCREEN_HEIGHT]

# display screen
window = pygame.display.set_mode(listScreen)

# position
pos = (500, 400)

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
        # constants for plotting schedule
        self.eventRing = (self.radius+self.innRadius)//2
        self.eventRadius = 5
        
    def Cartesian(self):
        # translated from time in day to x-y coordiantes
        # Given day and time, Returns Cartesian coordinates
        # use polar coordinates
        # theta = fraction of week * 2pi (in radians)
        
        # step 1: get polar
        self.eventRing = (self.radius+self.innRadius)//2
        self.today = datetime.datetime.today()
        self.start = week[0][1].weekday()
        LoA = []
        for i in range(len(week)):
            LoA += [[week[i][0] ,week[i][1].hour/24 + (week[i][1].weekday() - self.today.weekday())]]

        for i in range(len(LoA)):
            LoA[i][1] = LoA[i][1]/7*(2*3.14)
        
        # translate polar to cartesian
        # x = r × cos( θ )
        # y = r × sin( θ )
        for i in range(len(LoA)):
            LoA[i][1] = (self.eventRing*cos(LoA[i][1]),self.eventRing*sin(LoA[i][1]))

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
        
        for i in range(len(LoA)):
            pygame.draw.circle(window, PINK, LoA[i][1], self.eventRadius)


LoE = []
w = Week(LoE, pos)
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
