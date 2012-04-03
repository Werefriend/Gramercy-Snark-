#!/usr/bin/env python

import pygame

from settings import SCREEN_SIZE
from game import Game

def main():
    print "Helloooooo, nurse!"
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    game = Game(screen)
    game.run()
