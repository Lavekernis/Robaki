import pygame

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()
    clock.tick(60)