import pygame
import random

pygame.init()

#Game Window Setup
ScreenWidth = 600
ScreenHeight = 600
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Trash Collecting')

#Background Colors
sand = pygame.Color("#FFF0AD")
black = pygame.Color(0,0,0)

#Character Location + Dimensions
    #Character (x-coor, y-coord, width, height)
    #NOTE: Left-Right starts from 0 to 500
    #Up-Down starts from 0 to 500 as well
x = 50
y = 420
width = 100
height = 100
speed = 40

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        #Close window and end game            
        if event.type == pygame.QUIT:
            run = False
        
        #Get the key pressed by user
        keys = pygame.key.get_pressed()

        #Checks the key and moves the character correspondingly
        if keys[pygame.K_a] and x > speed:
            x -= speed
        elif keys[pygame.K_d] and x < ScreenWidth - width - speed:
            print(x)
            x += speed
        elif keys[pygame.K_w] and y > speed:
            y -= speed
        elif keys[pygame.K_s] and y < ScreenHeight - height - speed:
            y += speed

    #Load Background
    win.fill(sand)

    avatar = pygame.Rect(x, y, width, height)
    pygame.draw.rect(win, black, avatar)

    pygame.display.flip()
pygame.quit()