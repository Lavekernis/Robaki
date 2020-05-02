import game
import pygame
import variables as var


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((var.SCREEN_WIDTH, var.SCREEN_HEIGHT))
running = True


while running:

    frame_time = clock.get_time()

    screen.fill((0, 0, 0))
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # CAMERA SCROLLING
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            if x > var.SCREEN_WIDTH-var.SCROLLING_CONST:
                var.scroling_X_Inc = True
            else:
                var.scroling_X_Inc = False
            if x < var.SCROLLING_CONST:
                var.scroling_X_Dec = True
            else:
                var.scroling_X_Dec = False
            if y > var.SCREEN_HEIGHT-var.SCROLLING_CONST:
                var.scroling_Y_Inc = True
            else:
                var.scroling_Y_Inc = False
            if y < var.SCROLLING_CONST:
                var.scroling_Y_Dec = True
            else:
                var.scroling_Y_Dec = False

    # GAME UPDATE
    game.update(screen, frame_time)

    # DISPLAY UPDATE
    pygame.display.update()
    clock.tick(60)
