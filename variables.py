import pygame
import os

FILEPATH = os.path.dirname(__file__)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900


# CAMERA SCROLING VARIABLES
camera_vector = pygame.math.Vector2(0, 0)
scroling_X_Inc = False
scroling_X_Dec = False
scroling_X_Inc = False
scroling_X_Inc = False
SCROLLING_CONST = 20
SCROLLING_SPEED = 0.5
GRAVITY = 9.81

WORM_CRAWL_SPEED = 2

LEFT_ARROW_KEY_ID = 276
RIGHT_ARROW_KEY_ID = 275
UP_ARROW_KEY_ID = 273
DOWN_ARROW_KEY_ID = 274
SPACE_KEY_ID = 32
