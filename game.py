import variables as var
from pygame.math import Vector2
from map import *
from enum import Enum
import time
import worm

map = Map("Map.bmp", "background.bmp")
start = time.time()
map.remove_circle(Vector2(1200, 500), 150)
end = time.time()
print(end - start)



pygame.font.init()
font = font = pygame.font.SysFont("comicsansms", 48)
physic_objects_list = [worm.Worm((100,100)),worm.Worm((1500,1500))] 


class InputState(Enum):
    PRESSED = 1
    RELEASED = 2
    HELD = 3
    NO_ACTION = 4


class InputManager():

    def __init__(self):
        self._input_state = {275:InputState.NO_ACTION,274:InputState.NO_ACTION,32:InputState.NO_ACTION,276:InputState.NO_ACTION,277:InputState.NO_ACTION}

    def event_handler(self,event):
        """For given event.key change its state"""        
        if event.type == pygame.KEYDOWN:
            if event.key in self._input_state:
                if self._input_state[event.key] != InputState.PRESSED and self._input_state[event.key] != InputState.HELD:
                    self._input_state[event.key] = InputState.PRESSED
                    print(str(event.key)+" PRESSED") 
        elif event.type == pygame.KEYUP:
            if event.key in self._input_state:
                if self._input_state[event.key] == InputState.RELEASED:
                    self._input_state[event.key] = InputState.NO_ACTION
                    print(str(event.key)+" NO_ACTION")
                else:
                    self._input_state[event.key] = InputState.RELEASED 
                    print(str(event.key)+" RELEASED")
        for state in self._input_state.values():
            if state == InputState.PRESSED:
                state = InputState.HELD
                print(str(event.key)+" HELD")
                    

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

    #OBJECT_DRAWING_LOOP
    for obj in physic_objects_list:
        if obj.position[0] > var.camera_vector.x and obj.position[1] > var.camera_vector.y:
            x,y = round(obj.position[0] - var.camera_vector[0]),round(obj.position[1] - var.camera_vector[1])
            obj.draw(screen,(x,y))

    world_x = var.camera_vector.x + (var.SCREEN_WIDTH / 2)
    world_y = var.camera_vector.y + (var.SCREEN_HEIGHT / 2)
    screen_center = (round(var.SCREEN_WIDTH/2), round(var.SCREEN_HEIGHT / 2))
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
