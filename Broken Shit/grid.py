#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame import draw

#Declare some variables...------------------------------------------
pygame.init()

TILE_SIZE = 40
SCREEN_WIDTH = 20
SCREEN_HEIGHT = 20
SCREEN_SIZE = (TILE_SIZE*SCREEN_WIDTH, TILE_SIZE*SCREEN_HEIGHT)
BLACK = (0,0,0)
FOREST = (34,139,34)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE))
screen_bounds = screen.get_rect()
done = False
GRID = []
FPS = 20
GRAMERCY_PARK = []


#This a list of list of objects.
#Receives tile object, iterates it.---------------------------------

def grid():
    park = []
    for y in range(SCREEN_HEIGHT):
        row = []
        for x in range(SCREEN_WIDTH):
            cell = {}
            cell["pooped"] = False
            cell["rect"] = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            row.append(cell)
        park.append(row)
    return park

#program loop--------------------------------------------------------

# build world
GRAMERCY_PARK = grid()

while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True

    # update

    # draw
    for row in GRAMERCY_PARK:
        for cell in row:
            screen.fill(FOREST, cell["rect"])

    clock.tick(FPS)
    pygame.display.flip()
