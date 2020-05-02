import pygame
import os

filepath = os.path.dirname(__file__)


class Map():
    def __init__(self, path):
        """Initalizes map from bmp file"""
        self.surface = pygame.image.load(os.path.join(filepath, path))

    def draw(self, camera_offset, screen):
        #TODO: implement camera offset
        screen.blit(self.surface, (0, 0))
