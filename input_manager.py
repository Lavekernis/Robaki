from enum import Enum
import variables as var
import pygame


class InputState(Enum):
    PRESSED = 1
    RELEASED = 2
    HELD = 3
    NO_ACTION = 4


class InputManager():

    def __init__(self):
        self._input_state = {var.RIGHT_ARROW_KEY_ID: InputState.NO_ACTION,
                             var.DOWN_ARROW_KEY_ID: InputState.NO_ACTION,
                             var.SPACE_KEY_ID: InputState.NO_ACTION,
                             var.LEFT_ARROW_KEY_ID: InputState.NO_ACTION,
                             var.UP_ARROW_KEY_ID: InputState.NO_ACTION}

    def event_handler(self, event):
        """For given event.key change its state"""
        if event.type == pygame.KEYDOWN:
            if event.key in self._input_state:
                if self._input_state[event.key] != InputState.PRESSED and self._input_state[event.key] != InputState.HELD:
                    self._input_state[event.key] = InputState.PRESSED
                    # print(str(event.key)+" PRESSED")
        elif event.type == pygame.KEYUP:
            if event.key in self._input_state:
                if self._input_state[event.key] == InputState.RELEASED:
                    self._input_state[event.key] = InputState.NO_ACTION
                    # print(str(event.key)+" NO_ACTION")
                else:
                    self._input_state[event.key] = InputState.RELEASED
                    # print(str(event.key)+" RELEASED")
        for state in self._input_state.values():
            if state == InputState.PRESSED:
                state = InputState.HELD

    def is_key_held(self, key):
        return self._input_state[key] == InputState.HELD

    def is_key_pressed(self, key):
        return self._input_state[key] == InputState.PRESSED

    def is_key_released(self, key):
        return self._input_state[key] == InputState.RELEASED
