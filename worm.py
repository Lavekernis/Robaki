import pygame
from physicsobject import PhysicsObject
from pygame.math import Vector2
import game
import variables as var
import input_manager

class Worm(PhysicsObject):
    def __init__(self, pos, is_selected = False):
        self._is_firing = False
        self._is_selected = is_selected
        self._health = 100
        self._team = 0
        self._position = pos

    def draw(self,screen,pos):
        pygame.draw.circle(screen, (255, 0, 0), (round(pos.x),round(pos.y)), 10)
    
    def update(self,screen,frame_time):
        cor = super().camera_cord_converter()

        if self._equalibrium == False:
            self._acceleration = Vector2(0, var.GRAVITY)
            self._velocity += self._acceleration * frame_time
            self._position += self._velocity * frame_time
            if game.map.circle_collision(self._position, 10) != None:
                self._equalibrium = True
        

        if self._is_selected:
            inp = input_manager.InputManager.instance
            if inp.is_key_held(var.RIGHT_ARROW_KEY_ID):
                self._position.x += frame_time*var.WORM_CRAWL_SPEED
                # self._equalibrium = False
            
            
        
                
        self.draw(screen,cor)
