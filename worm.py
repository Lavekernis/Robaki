import pygame
from physicsobject import PhysicsObject
from pygame.math import Vector2
import game
import variables as var


class Worm(PhysicsObject):
    def __init__(self, pos):
        self._is_firing = False
        self._is_selected = False
        self._health = 100
        self._team = 0
        self._position = pos

    def update(self, frame_time):
        if self._equalibrium == False:
            self._acceleration = Vector2(0, var.GRAVITY)
            self._velocity += self._acceleration * frame_time
            self._position += self._velocity * frame_time
            if game.map.circle_collision(self._position, 10) != None:
                self._equalibrium = True

    def draw(self, screen, pos):
        pygame.draw.circle(screen, (255, 0, 0), pos, 10)
