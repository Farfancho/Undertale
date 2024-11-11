import pygame
from pygame.locals import *
pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("UNDERTALE")

player = pygame.Rect((300, 500, 50, 50))

run = True
while run:
    screen.fill((0,24,45))
    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    if key[pygame.K_DOWN] == True:
        player.move_ip(0,1)
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    if key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    #? When player moves in two ortogonal directions at the same time, it moves faster
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit() 