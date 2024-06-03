import pygame
pygame.init()

screenWidth = 500
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sprites Test")

class Spritesheet:
    #Holds the spritesheet
    def __init__(self,filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    #Read the spritesheet and get the sprite frame
    def get_sprite(self, x, y, w, h, scale):
        #Create empty image (rectangle) which will hold the sprite frame
        sprite = pygame.Surface((w,h))

        #Removes the transparency from the spritesheet
        sprite.set_colorkey((0,0,0))

        #Get the spritesheet, location of the empty image frame, and the portion of the spritesheet
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))

        #Increasing the scale of the picture (sprite image, [width, height])
        sprite = pygame.transform.scale(sprite, (w * scale, h * scale))
        return sprite
    
    #Getting a whole list of the sprite frames to animate
    def parse_sprite(self):
        standCount = 0
        standSprite = []
        while standCount < 48:
            spriteStand = self.sprite_sheet.get_sprite(standCount, 0, 24, 24)
            standCount += 24
            standSprite.append(spriteStand)
        return standSprite
    
#Create Spritesheet object named sheet
sheet = Spritesheet('doug.png')
#Retrieve one frame of the sprite
sprite1 = sheet.get_sprite(0, 0, 24, 24, 8)


run = True
while run:

    screen.fill("white")
    #Load the sprite image and place it in corresponding screen position
    screen.blit(sprite1, (150, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()