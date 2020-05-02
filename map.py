import variables as var
import os
import pygame
from collision_info import CollisionInfo
from pygame.math import Vector2
from math import sin, cos, pi


class Map():
    def __init__(self, path):
        """Initalizes map from bmp file"""
        self.surface = pygame.image.load(os.path.join(var.FILEPATH, path))

    def draw(self, screen):
        camera_image = (
            var.camera_vector[0], var.camera_vector[1], var.SCREEN_WIDTH, var.SCREEN_HEIGHT)
        screen.blit(self.surface, (0, 0), camera_image)

    def circle_collision(self, pos, radius, points=36, screen=None):
        """Checks intersection of circle given the radius and position.
        Creates n amount of points on the circle to calculate proper normal.
        Returns CollisionInfo if collided, None otherwise."""
        phi = 2 * pi / points
        intersects = []

        for i in range(0, points):
            point_coordinate = Vector2(sin(phi * i), cos(phi * i)) * radius
            point_coordinate += Vector2(pos.x, pos.y)

            rx = round(point_coordinate.x)
            ry = round(point_coordinate.y)

            # out of bounds check
            if rx >= self.surface.get_width() or rx < 0 or ry >= self.surface.get_height() or ry < 0:
                continue

            # (0,0,0) is black colour, currently used to symbolize terrain
            if self.surface.get_at((rx, ry)) == (0, 0, 0, 255):
                if screen != None:
                    pygame.draw.circle(screen, (255, 0, 255), (round(
                        rx - var.camera_vector.x), round(ry - var.camera_vector.y)), round(radius / 10))
                intersects.append(point_coordinate)

        if len(intersects) == 0:
            return None
        else:
            normal = Vector2(0)
            for item in intersects:
                normal -= (item - pos)
            normal = normal.normalize()
            return CollisionInfo(normal)
