import game
import pygame
import variables as var


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((var.SCREEN_WITH, var.SCREEN_HEIGHT))
running = True



while running:

    screen.fill((0, 0, 0))


    #EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #CAMERA SCROLLING
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            if x > var.SCREEN_WITH-20:
                var.scroling_X_Inc = True
            else:
                var.scroling_X_Inc = False
            if x < 20:
                var.scroling_X_Dec = True
            else:
                var.scroling_X_Dec = False
            if y > var.SCREEN_HEIGHT-20:
                var.scroling_Y_Inc = True
            else:
                var.scroling_Y_Inc = False
            if y < 20:
                var.scroling_Y_Dec = True
            else:
                var.scroling_Y_Dec = False
            

    #GAME UPDATE
    game.update(screen)
    
    #DISPLAY UPDATE
    pygame.display.update()
    clock.tick(60)
