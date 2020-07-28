import variables as var
from pygame.math import Vector2
from map import *
from enum import Enum
import time
from worm import Worm
from team_manager import TeamManager

map = Map("Map.bmp", "background.bmp")
map.remove_circle(Vector2(1200, 500), 150)

pygame.font.init()
TeamManager()
font = pygame.font.SysFont("comicsansms", 48)
physic_objects_list = [Worm((100, 100)), Worm((1500, 1500))]


def cameraScrolling(frame_time: float):
    if var.scroling_X_Inc and var.camera_vector.x + var.SCREEN_WIDTH < map.surface.get_width():
        var.camera_vector.x += var.SCROLLING_SPEED * frame_time
        if var.camera_vector.x + var.SCREEN_WIDTH > map.surface.get_width():
            var.camera_vector.x = map.surface.get_width() - var.SCREEN_WIDTH
    if var.scroling_X_Dec and var.camera_vector.x > 0:
        var.camera_vector.x -= var.SCROLLING_SPEED * frame_time
        if var.camera_vector.x < 0:
            var.camera_vector.x = 0
    if var.scroling_Y_Inc and var.camera_vector.y + var.SCREEN_HEIGHT < map.surface.get_height():
        var.camera_vector.y += var.SCROLLING_SPEED * frame_time
        if var.camera_vector.y + var.SCREEN_HEIGHT > map.surface.get_height():
            var.camera_vector.y = map.surface.get_height() - var.SCREEN_HEIGHT
    if var.scroling_Y_Dec and var.camera_vector.y > 0:
        var.camera_vector.y -= var.SCROLLING_SPEED * frame_time
        if var.camera_vector.y < 0:
            var.camera_vector.y = 0


def update(screen: pygame.display, frame_time: float):
    cameraScrolling(frame_time)
    map.draw(screen)

    for obj in physic_objects_list:
        obj.update(screen, frame_time)

    world_x = var.camera_vector.x + (var.SCREEN_WIDTH / 2)
    world_y = var.camera_vector.y + (var.SCREEN_HEIGHT / 2)
    screen_center = (round(var.SCREEN_WIDTH/2), round(var.SCREEN_HEIGHT / 2))
    radius = 50

    text = font.render("X: " + str(round(world_x)) + " Y:" +
                       str(round(world_y)), True, (0, 128, 128))

    pygame.draw.circle(screen, (255, 0, 0), screen_center, radius)

    info = map.circle_collision(Vector2(world_x, world_y), radius, screen)
    if info != None:
        text2 = font.render("Normal: (" + str(round(info.normal.x)) +
                            ", " + str(round(info.normal.y)) + ")", True, (0, 128, 128))
        screen.blit(text2, (0, 48 + 5))

    screen.blit(text, (0, 0))


def add_worm(pos: Vector2, team: int):
    w = Worm(pos)
    physic_objects_list.append(w)
    TeamManager.instance.add_worm(w, team)
