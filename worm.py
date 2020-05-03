import pygame
import physicsobject
import variables as var

class Worm(physicsobject.PhysicsObject):
    def __init__(self,pos):
        self._is_firing = False
        self._is_selected = False
        self._health = 100
        self._team = 0
        self._position = pos
    
    def draw(self,screen,pos):
        pygame.draw.circle(screen, (255, 0, 0), pos, 10)
    