import pygame
import variables as var


class Map():
    def __init__(self, path):
        """Initalizes map from bmp file"""
        self.surface = pygame.image.load(var.os.path.join(var.filepath, path))
    def draw(self, screen):
        camera_image = (var.camera_vector[0],var.camera_vector[1],var.SCREEN_WITH,var.SCREEN_HEIGHT)
        screen.blit(self.surface, (0, 0),camera_image)
