import variables as var
from map import *

map = Map("Map.bmp")

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

def update(screen,frame_time):
    cameraScrolling(frame_time)
    map.draw(screen)