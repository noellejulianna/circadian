# goal: understand pygame

# format of calender
# draw a bunch of rectangles per day
# pull data from calender, make Day Class
# month class-> lis tof days, each day a day class, each list
# of days has information of what's scheduled on that day
# draw function in maonth class
# draw dunciton in each day class

# do draw funciton for day cirlce

import math
import pygame
pygame.init()


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
        self.Sunday = (pos[0], pos[1] + self.radius)
        self.Monday = (pos[0] + self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        self.Tuesday = (pos[0] + self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.Wednesday = (pos[0] + self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.Thursday = (pos[0] - self.radius*math.sin(math.radians(25.8+180)), pos[1] + self.radius*math.cos(math.radians(25.8+180)))
        self.Friday = (pos[0] - self.radius*math.cos(math.radians(12.8+180)), pos[1] + self.radius*math.sin(math.radians(12.8+180)))
        self.Saturday = (pos[0] - self.radius*math.sin(math.radians(51.4+180)), pos[1] - self.radius*math.cos(math.radians(51.4+180)))
        # constants for plotting schedule
        self.eventRing = (self.radius+self.innRadius)//2
        self.day = 24
        self.eventRadius = 5
        self.start = 0
        self.today = self.start + n

    def draw(self):
        """Draws the days and events of this week"""
        pygame.draw.circle(window, self.color, self.position, self.radius)
        pygame.draw.line(window, WHITE, self.position, self.Sunday)
        pygame.draw.line(window, WHITE, self.position, self.Monday)
        pygame.draw.line(window, WHITE, self.position, self.Tuesday)
        pygame.draw.line(window, WHITE, self.position, self.Wednesday)
        pygame.draw.line(window, WHITE, self.position, self.Thursday)
        pygame.draw.line(window, WHITE, self.position, self.Friday)        
        pygame.draw.line(window, WHITE, self.position, self.Saturday)
        pygame.draw.circle(window, self.inncolor, self.position, self.innRadius)
        # draw events as dots
        pygame.draw.circle(window, PINK, (pos[0]+10, pos[1]+10), self.eventRadius)


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
