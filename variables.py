import pygame
import os
from pygame.math import Vector2

FILEPATH = os.path.dirname(__file__)

SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 900


# CAMERA SCROLING VARIABLES
camera_vector: Vector2 = Vector2(0, 0)
scroling_X_Inc: bool = False
scroling_X_Dec: bool = False
scroling_X_Inc: bool = False
scroling_X_Inc: bool = False
SCROLLING_CONST: float = 20
SCROLLING_SPEED: float = 500
GRAVITY: float = 9.81

WORM_CRAWL_SPEED: float = 2

LEFT_ARROW_KEY_ID: int = 276
RIGHT_ARROW_KEY_ID: int = 275
UP_ARROW_KEY_ID: int = 273
DOWN_ARROW_KEY_ID: int = 274
SPACE_KEY_ID: int = 32
