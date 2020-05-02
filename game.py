import variables as var
from pygame.math import Vector2
from map import *

map = Map("Map.bmp")

pygame.font.init()
font = font = pygame.font.SysFont("comicsansms", 48)


def cameraScrolling():
    if var.scroling_X_Inc and var.camera_vector.x + var.SCREEN_WITH < map.surface.get_width():
        var.camera_vector.x += 10
    if var.scroling_X_Dec and var.camera_vector.x > 0:
        var.camera_vector.x -= 10
    if var.scroling_Y_Inc and var.camera_vector.y + var.SCREEN_HEIGHT < map.surface.get_height():
        var.camera_vector.y += 10
    if var.scroling_Y_Dec and var.camera_vector.y > 0:
        var.camera_vector.y -= 10


def update(screen):
    cameraScrolling()
    map.draw(screen)

    world_x = var.camera_vector.y + (var.SCREEN_WITH/2)
    world_y = var.camera_vector.x + (var.SCREEN_HEIGHT / 2)
    screen_center = (round(var.SCREEN_WITH/2), round(var.SCREEN_HEIGHT / 2))
    radius = 50

    text = font.render("X: " + str(round(world_x)) + " Y:" +
                       str(round(world_y)), True, (0, 128, 128))

    pygame.draw.circle(screen, (255, 0, 0), screen_center, radius)

    info = map.circle_collision(Vector2(world_x, world_y), radius)
    if info != None:
        text2 = font.render("Normal: (" + str(round(info.normal.x)) +
                            ", " + str(round(info.normal.y)) + ")", True, (0, 128, 128))
        pygame.draw.line(screen, (0, 255, 0), screen_center,
                         screen_center + (info.normal * radius), 5)
        screen.blit(text2, (0, 48 + 5))

    screen.blit(text, (0, 0))
