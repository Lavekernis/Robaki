import variables as var
from map import *

map = Map("Map.bmp")

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