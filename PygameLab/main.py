# File name: main.py (Driver of Drawable class) - Pygame window name: Snowfall
# Purpose: Uses drawable objects to create a pretty snowfall scene
# Author: Dan Dowlin
# Version 5/4/2023


import pygame, sys
from pygame.locals import *
from Drawable import *
from random import randint

# Initialize pygame window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Snowfall')

# Create drawable objects
ground = Rectangle(0, 300, 400, 300, (86, 125, 70))
ground.draw(DISPLAYSURF)

sky = Rectangle(0, 0, 400, 300, (135, 206, 235))
sky.draw(DISPLAYSURF)

# Creates drawable list to update screen and adds ground and sky
drawables = [ground, sky]
animating = True

while True: # main game loop
    # While animating, draw all drawables
    if animating == True:
        for drawable in drawables:
            drawable.draw(DISPLAYSURF)
            # If it is a snowflake and hasn't reached its max Y
            if isinstance(drawable, Snowflake) and not drawable.getLoc()[1] == drawable.getMaxY():
                drawable.setLoc((drawable.getLoc()[0], drawable.getLoc()[1] + 1))
        # Create new snowflake and add it to drawables    
        newSnowflake = Snowflake(randint(0, 400))
        drawables.append(newSnowflake)
    
    for event in pygame.event.get():
        # When the user gets space, toggle animation status
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                animating = not animating
        
        #Close out of the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  
    pygame.display.update() # Update all visual components
