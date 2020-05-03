import variables as var
from pygame.math import Vector2
from map import *
import time
import worm

map = Map("Map.bmp", "background.bmp")
map.remove_circle(Vector2(1200, 500), 150)


pygame.font.init()
font = font = pygame.font.SysFont("comicsansms", 48)
physic_objects_list = [worm.Worm((100, 100)), worm.Worm((1500, 1500))]


def cameraScrolling(frame_time):
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


def update(screen, frame_time):
    cameraScrolling(frame_time)
    map.draw(screen)

    # Physics Object List Handling
    for obj in physic_objects_list:
        obj.update(frame_time)
        if obj.position[0] > var.camera_vector.x and obj.position[1] > var.camera_vector.y:
            x, y = round(obj.position[0] - var.camera_vector[0]
                         ), round(obj.position[1] - var.camera_vector[1])
            obj.draw(screen, (x, y))

    # Collision Debugging
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
