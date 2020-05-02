import variables as var
from pygame.math import Vector2
from map import *

map = Map("Map.bmp")
print(map.surface.get_at((0, 0)))
print(map.surface.get_at((622, 438)))
print(map.surface.get_at((623, 439)))

pygame.font.init()
font = font = pygame.font.SysFont("comicsansms", 48)


def cameraScrolling(frame_time):
    if var.scroling_X_Inc and var.camera_vector.x + var.SCREEN_WITH < map.surface.get_width():
        var.camera_vector.x += var.SCROLLING_SPEED * frame_time
        if var.camera_vector.x + var.SCREEN_WITH > map.surface.get_width():
            var.camera_vector.x = map.surface.get_width() - var.SCREEN_WITH
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

    world_x = var.camera_vector.x + (var.SCREEN_WITH/2)
    world_y = var.camera_vector.y + (var.SCREEN_HEIGHT / 2)
    screen_center = (round(var.SCREEN_WITH/2), round(var.SCREEN_HEIGHT / 2))
    radius = 50

    text = font.render("X: " + str(round(world_x)) + " Y:" +
                       str(round(world_y)), True, (0, 128, 128))

    pygame.draw.circle(screen, (255, 0, 0), screen_center, radius)

    info = map.circle_collision(Vector2(world_x, world_y), radius, 36, screen)
    if info != None:
        text2 = font.render("Normal: (" + str(round(info.normal.x)) +
                            ", " + str(round(info.normal.y)) + ")", True, (0, 128, 128))
        pygame.draw.line(screen, (0, 255, 0), screen_center,
                         screen_center + (info.normal * radius), 5)
        screen.blit(text2, (0, 48 + 5))

    screen.blit(text, (0, 0))
