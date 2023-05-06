#File Name:   Drawable.py
#Purpose:     Abstract class and derived classes that allows us to create drawable objects
#             with different shapes, at a given location (x, y)
#Last update: 5/4/23 - D. Dowlin

import pygame
from abc import ABC, abstractmethod
from random import randint

class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface):
        pass

class Rectangle(Drawable):
    def __init__(self, x = 0, y = 0, width = 0, height = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getColor(self):
        return self.__color

    '''
        Draws the rectangle to a given surface
    '''
    def draw(self, surface):
        pygame.draw.rect(surface, self.getColor(), pygame.Rect(self.getLoc()[0], self.getLoc()[1], self.getWidth(), self.getHeight()))

class Snowflake(Drawable):
    def __init__(self, x = 0):
        super().__init__(x, y = 0)
        #Maximumum distance the snowflake can travel
        self.__maxY = (randint(300, 500))
    
    '''
        Gets the max distance the snowflake can travel
    '''
    def getMaxY(self):
        return self.__maxY

    '''
        Draws a 4-line snowflake to a given surface
    '''
    def draw(self, surface):
        x = self.getLoc()[0]
        y = self.getLoc()[1]
        WHITE = (255, 255, 255)

        pygame.draw.line(surface, WHITE, (x-5, y), (x+5, y))
        pygame.draw.line(surface, WHITE, (x, y-5), (x, y+5))
        pygame.draw.line(surface, WHITE, (x-5, y-5), (x+5, y+5))
        pygame.draw.line(surface, WHITE, (x-5, y+5), (x+5, y-5))