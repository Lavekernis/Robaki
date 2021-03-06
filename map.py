import variables as var
import os
import pygame
from collision_info import CollisionInfo
from pygame.math import Vector2
from math import sin, cos, pi


class Map():
    def __init__(self, map_path: str, background_path: str):
        """Initalizes map from bmp file"""
        self.surface = pygame.image.load(os.path.join(var.FILEPATH, map_path))
        self.background = pygame.image.load(
            os.path.join(var.FILEPATH, background_path))
        # white being transparent
        self.surface.set_colorkey((255, 255, 255, 255))

    def draw(self, screen: pygame.display):
        screen.blit(self.background, (0, 0))
        camera_image = (
            var.camera_vector[0], var.camera_vector[1], var.SCREEN_WIDTH, var.SCREEN_HEIGHT)
        screen.blit(self.surface, (0, 0), camera_image)

    def circle_collision(self, pos: Vector2, radius: float, screen=None, points=36):
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

            # Isn't white, which represents lack of terrain
            if self.surface.get_at((rx, ry)) != (255, 255, 255, 255):
                if screen != None:
                    pygame.draw.circle(screen, (255, 0, 255), (round(
                        rx - var.camera_vector.x), round(ry - var.camera_vector.y)), round(radius / 10))
                intersects.append(point_coordinate)

        if len(intersects) == 0 or len(intersects) == points:
            return None
        else:
            normal = Vector2(0)
            for item in intersects:
                normal -= (item - pos)
            normal = normal.normalize()
            if screen != None:
                pygame.draw.line(screen, (0, 255, 0), (round(
                    pos.x - var.camera_vector.x), round(pos.y - var.camera_vector.y)),
                    (round(
                        pos.x - var.camera_vector.x), round(pos.y - var.camera_vector.y)) + (normal * radius), 5)
            return CollisionInfo(normal, pos)

    def circlecast_collision(self, pos: Vector2, direction: Vector2, range: float, radius: float, screen: pygame.display = None):
        destination = direction.normalize() * range
        length = destination.length()
        dx = destination.x / length
        dy = destination.y / length
        for i in range(0, round(length)):
            rx = round(dx * i)
            ry = round(dy * i)
            info = self.circle_collision(Vector2(rx, ry), radius, screen)
            if info != None:
                return info
        return None

    def remove_circle(self, pos: Vector2, radius: float):
        # If turns out too slow use PixelArray
        top_left = Vector2(pos.x - radius, pos.y - radius)
        bottom_right = Vector2(pos.x + radius, pos.y + radius)

        # oob check for both points
        if top_left.x < 0:
            top_left.x = 0
        if top_left.x >= self.surface.get_width():
            top_left.x = self.surface.get_width()
        if top_left.y < 0:
            top_left.y = 0
        if top_left.y >= self.surface.get_height():
            top_left.y = self.surface.get_height()
        if bottom_right.x < 0:
            bottom_right.x = 0
        if bottom_right.x >= self.surface.get_width():
            bottom_right.x = self.surface.get_width()
        if bottom_right.y < 0:
            bottom_right.y = 0
        if bottom_right.y >= self.surface.get_height():
            bottom_right.y = self.surface.get_height()

        for dx in range(round(top_left.x), round(bottom_right.x)):
            for dy in range(round(top_left.y), round(bottom_right.y)):
                if Vector2(dx, dy).distance_to(pos) > radius:
                    continue
                else:
                    self.surface.set_at((dx, dy), (255, 255, 255))
