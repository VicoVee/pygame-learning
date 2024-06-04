import pygame
import random
import sprite

pygame.init()

#Game Window Setup
ScreenWidth = 600
ScreenHeight = 600
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Trash Collecting')

#Background Colors
sand = pygame.Color("#FFF0AD")
black = pygame.Color(0,0,0)
purple = pygame.Color("#A115B3")

#Getting the Character Sprite
#Load in the spritesheet
doug_sheet = sprite.Spritesheet('doug.png')
#Take a single frame from the spritesheet
frame0 = doug_sheet.get_frame(1,0,0,24,24,3)

#Creating Sprite animation
#Holds a list of all frames in the animation
frameList = []
#I want the first four frames, so indicated by this variable
frame_steps = 4
#A timer to track the frames and play them correctly
last_update = pygame.time.get_ticks()
frame_cooldown = 200
start_frame = 0

#Collects the 4 frames I want and place into the frameList
for i in range(frame_steps):
    frameList.append(doug_sheet.get_frame(i, 0, 0, 24, 24, 3))

#Character Location + Dimensions
    #Character (x-coor, y-coord, width, height)
    #NOTE: Left-Right starts from 0 to 500
    #NOTE: Up-Down starts from 0 to 500 as well
char_x = 50
char_y = 460
char_width = frame0.get_width()
char_height = frame0.get_height()
char_speed = 30

#Window Boundaries
WidthBoundary = ScreenWidth - char_width - char_speed
HeightBoundary = ScreenHeight - char_height - char_speed

#Make a list of interactive trash sprites
TrashPile= []
for i in range(10):
    #Randomly assign a size and location of each piece of trash
    trash_x = random.randint(5, ScreenWidth - 100)
    trash_y = random.randint(5, ScreenHeight - 100)
    trash_w = random.randint(20, 50)
    trash_h = random.randint(20, 80)
    #Create and add them to the TrashPile list
    trash = pygame.Rect(trash_x,trash_y,trash_w,trash_h)
    TrashPile.append(trash)

run = True
while run:
    #Delay the game loading
    pygame.time.delay(100)

    for event in pygame.event.get():
        #Close window and end game            
        if event.type == pygame.QUIT:
            run = False
        
        #Get the key pressed by user
        keys = pygame.key.get_pressed()

        #Checks the key and moves the character correspondingly
        if keys[pygame.K_a] and char_x > char_speed:
            char_x -= char_speed
        elif keys[pygame.K_d] and char_x < WidthBoundary:
            char_x += char_speed
        elif keys[pygame.K_w] and char_y > char_speed:
            char_y -= char_speed
        elif keys[pygame.K_s] and char_y < HeightBoundary:
            char_y += char_speed

    #Load/Update Background
    win.fill(sand)

   #Load the trash in
    for trash in TrashPile:
        pygame.draw.rect(win, purple, trash)

    #~~~ Update frame animation ~~~
    #Get the current ingame time
    current_time = pygame.time.get_ticks()
    #Check the duration between frames. If the frame cooldown is over, get the next frame and reset the cooldown
    if current_time - last_update >= frame_cooldown:
        start_frame += 1
        last_update = current_time
    #When all frames are played, reset to the starting frame
    if start_frame >= len(frameList):
        start_frame = 0
        
    # char = pygame.Rect(char_x, char_y, char_width, char_height)
    # pygame.draw.rect(win, black, char)
    #Instead of a rectangle, it been replace with a single frame from the sprite sheet

    #Show frame
    win.blit(frameList[start_frame], (char_x, char_y))

    pygame.display.flip()
pygame.quit()