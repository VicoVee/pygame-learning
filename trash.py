import pygame
import random
import sprite

pygame.init()

#Game Window Setup
ScreenWidth = 600
ScreenHeight = 600
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Doug Eat Cookies')

#Background Colors
sand = pygame.Color("#FFF0AD")
black = pygame.Color(0,0,0)
purple = pygame.Color("#A115B3")

# ~~ Methods ~~
def redrawGameWindow():
    global set

    #Load/Update Background
    win.fill(sand)
    
    #Load the Cookie in
    #Cookie = (0:surface_img, 1:(x,y coordinates), 2:Rectangle food_hitbox)
    for cookie in CookiePile:
        pygame.draw.rect(win, "red", cookie[2])
        win.blit(cookie[0], cookie[1])

    char_hitbox = pygame.Rect(char_x + 40, char_y + 20, char_width-80, char_height-35)
    pygame.draw.rect(win, purple, char_hitbox)

    if pygame.Rect.collidelist(char_hitbox, CookieList) != -1:
        deleteCookie = char_hitbox.collidelist(CookieList)
        print(deleteCookie)
        # CookiePile.pop(deleteCookie)

    #Show frame
    if current_set == 1 and left == True:
        win.blit(frameWalkLeft[current_frame], (char_x, char_y))
    elif current_set == 1 and right == True:
        win.blit(frameWalkRight[current_frame], (char_x, char_y))
    else:
        win.blit(frameStand[current_frame], (char_x, char_y))
    
    #Update Window
    pygame.display.flip()

# ~~ Getting the Character Sprite ~~
#Load in the spritesheet
doug_sheet = sprite.Spritesheet('doug.png')
food_sheet = sprite.Spritesheet('Food.png')

# ~~ Character Location + Dimensions ~~
    #Character (x-coor, y-coord, width, height)
    #NOTE: Left-Right starts from 0 to 500
    #NOTE: Up-Down starts from 0 to 500 as well
char_x = 50
char_y = 460
char_speed = 15
char_scale = 5
left = None
right = None

#Take a single frame from the spritesheet
frame0 = doug_sheet.get_frame(1,0,0,24,24, char_scale)

char_width = frame0.get_width()
char_height = frame0.get_height()


# ~~ Creating Sprite animation ~~
#Holds a list of all frames in the animation
frameStand = []
frameWalkLeft = []
frameWalkRight = []
#Holds the start from the set of animations in the sprite sheet 
#(stand, run, jump, [Not Added here] injured, and crouch)
frameSet = [4, 6, 4]
#Holds the current animation to run from frameSet
#0 = stand; 1 = runLeft, 2 = runRight
current_set = 0
#A timer to track the frames and play them correctly
last_update = pygame.time.get_ticks()
#Tracks how long each frame should play before loading the next frame
frame_cooldown = 100
#Track the current frame in frameList
current_frame = 0

#Collects all the frames based on the selected frameSet
for i in range(frameSet[0]):
    frameStand.append(doug_sheet.get_frame(i, 0, 0, 24, 24, char_scale))

for i in range(frameSet[1]):
    frameWalkLeft.append(doug_sheet.get_frame(i + frameSet[0], 0, 0, 24, 24, char_scale))

for i in range(len(frameWalkLeft)):
    frameWalkRight.append(pygame.transform.flip(frameWalkLeft[i], True, False))


#Window Boundaries
WidthBoundary = ScreenWidth - char_width - char_speed
HeightBoundary = ScreenHeight - char_height - char_speed


#Make a list of interactive cookie sprites
CookiePile= []
CookieList = []
for i in range(10):
     #Get the cookie sprite image
    food0 = food_sheet.get_frame(0,0,0,16, 16,3)

    #Randomly assign a location of each cookie sprite
    food_x = random.randint(char_speed, ScreenWidth - 150)
    food_y = random.randint(char_speed, ScreenHeight - 150)

    #Get the width and height of the cookie sprite
    food_w = food0.get_width()
    food_h = food0.get_height()

    #Create hitbox
    food_hitbox = pygame.Rect(food_x + 5, food_y + 5, food_w - 10, food_h - 10)

    #Add the image and the randomly generated coordinates as a pair in the list.
    CookiePile.append((food0, (food_x, food_y), food_hitbox))
    CookieList.append(food_hitbox)


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
            left = False
            right = True
            current_set = 1
        elif keys[pygame.K_d] and char_x < WidthBoundary:
            char_x += char_speed
            left = True
            right = False
            current_set = 1
        elif keys[pygame.K_w] and char_y > char_speed:
            char_y -= char_speed
            left = True
            right = False
            current_set = 1
        elif keys[pygame.K_s] and char_y < HeightBoundary:
            char_y += char_speed
            left = True
            right = False
            current_set = 1
        else:
            current_set = 0

    #~~~ Update frame animation ~~~
    #Get the current ingame time
    current_time = pygame.time.get_ticks()
    #Check the duration between frames. If the frame cooldown is over, get the next frame and reset the cooldown
    if current_time - last_update >= frame_cooldown:
        current_frame += 1
        last_update = current_time
    #When all frames are played, reset to the starting frame
    if current_frame >= frameSet[current_set]:
        current_frame = 0
        
    redrawGameWindow()
pygame.quit()



