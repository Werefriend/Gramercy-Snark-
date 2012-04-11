#!/usr/bin/env python

import pygame
from pygame.locals import *

#from pygame import nothing!
#Just kidding
#Piper Odegard, Sam Reeves :in:
#Gramercy Snark!


##Settings
FPS = 60

##Colors
WHITE = 255,255,255
BLACK = 0,0,0

#Teh Game
def game(tile, width, height):
    #init
    screen = pygame.display.set_mode((width*tile, height*tile))

    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["cleared"] = False #Cell becomes cleared when it is hit by poo
            row.append(cell)
        world.append(row) #Code copied from minesweeper

"""

        #Poo on the square does:
        c = 0
        while c < num_targets:
            x = randrange(width)
            y = randrange(height)
            if not world[x][y]["target"]:
                world[x][y]["target"] = True
                c+=1
                #if not already a target, make a target.

"""


        #Display
        screen.fill(BLACK)
        for x in range(width):
            for y in range(height):
                rect = world[x][y]["rect"]

                #cell color
                if world[x][y]["cleared"]:
                    bg_color = (23,134,35)
                    

                #draw background
                screen.fill(bg_color, rect.inflate(-3,-3))
                


            #REFRESH DAMMIT!
            pygame.display.flip()
            clock.tick(FPS)
        
#Application
def main():
    pygame.init()
    game(50,10,10)

main()
print "Running away, are we?"


"""

        #LOOP
        clock = pygame.init.Clock()
        done = False
        while not done:
            #input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                
                #Loose the poo
                elif event.type = MOUSEBUTTONDOWN and event.button == 1:
                    
                #Movement?
                elif event.type == KEYDOWN and event.button = K_w:
                    
elif event.type == KEYDOWN and event.button = K_w:
elif event.type == KEYDOWN and event.button = K_w:
elif event.type == KEYDOWN and event.button = K_w:
            
"""


