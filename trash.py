import pygame
import random

pygame.init()

#Game Window Setup
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Trash Collecting')

#Background
sand = pygame.Color("#FFF0AD")
black = pygame.Color(0,0,0)

run = True
while run:
    win.fill(sand)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()