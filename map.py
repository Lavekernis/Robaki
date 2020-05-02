import pygame
import pygame.math
import numpy as np
from collision_info import CollisionInfo
import os

filepath = os.path.dirname(__file__)


class Map():
    def __init__(self, path):
        """Initalizes map from bmp file"""
        self.surface = pygame.image.load(os.path.join(filepath, path))

    def draw(self, camera_offset, screen):
        # TODO: implement camera offset
        screen.blit(self.surface, (100, 0))

    def circle_collision(self, pos, radius, points=36):
        """Checks intersection of circle given the radius and position. Creates n amount of points on the circle to calculate proper normal."""
        phi = 360.0 / points
        intersects = []

        for i in range(0, points):
            point_coordinate = (round(sin(phi * i)) * radius,
                                round(cos(phi * i)) * radius)
            point_coordinate += Vector2(round(pos.x), round(pos.y))

            # out of bounds check
            if point_coordinate.x >= self.surface.get_width() or point_coordinate.x < 0 or point_coordinate.y >= self.surface.get_height() or point_coordinate.y < 0:
                continue

            # (0,0,0) is black colour, currently used to symbolize terrain
            if self.surface.get_at(point_coordinate) == (0, 0, 0):
                intersects.append(point_coordinate)

        if len(intersects) == 0:
            return None
        else:
            normal = Vector2(0)
            for item in intersects:
                normal -= item
            normal = normal.normalize()
            return CollisionInfo(normal)
