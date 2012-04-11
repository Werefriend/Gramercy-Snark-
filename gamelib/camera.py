#!/usr/bin/env python

from pygame import Rect

from util import rel_rect

class Camera(object):
    def __init__(self, level, player, size):
        self.level = level
        self.player = player
        self.rect = Rect((0,0), size)
        
    def update(self):
        self.rect.center = self.player.rect.center
        if self.rect.top < self.level.bounds.top:
            self.rect.top = self.level.bounds.top
        if self.rect.bottom > self.level.bounds.bottom:
            self.rect.bottom = self.level.bounds.bottom

        if self.rect.left < self.level.bounds.left:
            self.rect.left = self.level.bounds.left
        if self.rect.right > self.level.bounds.right:
            self.rect.right = self.level.bounds.right

    def draw_level(self, surf):
        surf.blit(self.level.background, (-self.rect.x, -self.rect.y))

    def draw_player(self, surf):
        self.draw_sprite(surf, self.player)

    def draw_sprite(self, surf, sprite):
        surf.blit(sprite.image, rel_rect(sprite.rect, self.rect))
