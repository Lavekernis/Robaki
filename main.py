import pygame
from map import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
running = True

map = Map("Map.bmp")

while running:

    screen.fill((0, 0, 0))
    map.draw((0,0), screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
