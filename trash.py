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

#Character Location + Dimensions
    #Character (x-coor, y-coord, width, height)
    #NOTE: Left-Right starts from 0 to 500
    #Up-Down starts from 0 to 500 as well
char_x = 50
char_y = 460
char_width = 50
char_height = 100
char_speed = 40

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

    #Testing the sprite class
    doug_sheet = sprite.Spritesheet('doug.png')
    frame0 = doug_sheet.get_frame(0,0,0,24,24,5)

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

    #Load Background
    win.fill(sand)

   #Load the trash in
    for trash in TrashPile:
        pygame.draw.rect(win, purple, trash)

    # char = pygame.Rect(char_x, char_y, char_width, char_height)
    # pygame.draw.rect(win, black, char)
    win.blit(frame0, (char_x, char_y))

    pygame.display.flip()
pygame.quit()