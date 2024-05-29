import pygame
import random

#Start Pygame
pygame.init()

#Window Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

#create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#display the name of the game window
pygame.display.set_caption('Tester')

#Defines when the box is being moved 
active = None

#creating a single box
box = pygame.Rect(20,20,20,20)

#toggles when game is on or off
run = True
while run:
    #Color the window blue
    screen.fill("turquoise1")

    #Draw the box
    pygame.draw.rect(screen, "purple", box)

    #When the player ends the game, change run to False to end loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

#End the program
pygame.quit()