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

#Defines when the box is being moved. None is the same as NULL
active = None

#Creates a rectangle (left, top, width, height)
#We will call this box 1
box = pygame.Rect(50,50,50,50)

#toggles when game is on or off
run = True
while run:
    #Color the window blue
    screen.fill("turquoise1")

    #Draw the box
    pygame.draw.rect(screen, "purple", box)

    #Event = Checks any interaction with the screen: Exiting, MouseDown, Mouse Click
    for event in pygame.event.get():
        #When the LEFT mouse button is click and held down
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1: #Signifies the left mouse button being down
              #Check if the box collides with the mouse/clicked by mouse
              #Pos, the position of the box
              if box.collidepoint(event.pos): 
                  #Toggle the box to be active.
                  active = 'on'

        #Tracks the location of the mouse
        if event.type == pygame.MOUSEMOTION:
            if active != None:
                box.move_ip(event.rel)

        if event.type == pygame.QUIT:
            run = False

    #Update the contents of the WHOLE screen
    pygame.display.flip()
    #pygame.display.update() can update a portion or the whole screen depending on parameters

#End the program
pygame.quit()