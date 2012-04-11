#!/usr/bin/env python

import pygame
from pygame.locals import *

from settings import FPS
from camera import Camera
from level import Level
from player import Player


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.level = Level()
        self.player = Player(self.level)
        self.cam = Camera(self.level, self.player, self.screen.get_size())

    def quit(self):
        self.done = True

    def update(self):
        dt = self.clock.tick(FPS)
        self.player.update(dt)
        self.cam.update()

    def draw(self):
        self.cam.draw_level(self.screen)
        self.cam.draw_player(self.screen)

    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()

        while not self.done:

            #input
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit()

            self.update()
            self.draw()
            pygame.display.flip()
