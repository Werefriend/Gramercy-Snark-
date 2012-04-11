#!/usr/bin/env python

import pygame, os
from pygame.locals import *
from pygame import Rect, Surface

from settings import LEVEL_SIZE

class Level(object):
    def __init__(self):
        self.bounds = Rect((0,0), LEVEL_SIZE)
        self.render_background()

    def render_background(self):
        self.background = Surface(self.bounds.size)

        rows = self.bounds.height/20
        cols = self.bounds.width/20

        self.background.fill((0, 0, 0))
        for y in range(rows):
            for x in range(cols):
                self.background.fill((80, 80, 80), (x*20 +2, y*20 +2, 18, 18))
