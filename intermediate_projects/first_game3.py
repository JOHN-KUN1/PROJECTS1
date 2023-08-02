# STARTING PYGAME(ANIMATION AND SPRITES)

import pygame
pygame.init()

win = pygame.display.set_mode((500, 450))
pygame.display.set_caption('My First Game')

# STEP 2: LOAD THE IMAGES
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 45
y = 350
height = 64
width = 64
vel = 5


isJump = False
jumpCount = 10

# STEP 1: DETERMINE IF THE CHARACTER IS WALKING AND ITS WALK COUNT
left = False
right = False
walkCount = 0

# STEP 3: CREATE FUNCTION TO DRAW THE GAME WINDOW AND CHARACTER: 1. PUT A PICTURE ON THE SCREEN


def windowImage():
    global walkCount
    win.blit(bg, (0, 0))
# STEP 7: REMOVE THE RECTANGLE CODE AND WRITE CONDITIONAL FOR THAT DRAWS THE OBJECT BASED ON THE POSITION ITS MOVING

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


run = True
while run:
    # UPDATE THE FRAME RATE
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
# STEP 5 : CHANGE THE VARIABLE FOR LEFT AND RIGHT BASED ON THE KEY PRESS DIRECTION
        left = False
        right = True
    elif keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
# STEP 6 : WRITE AN ELSE STATEMENT FOR IF NON OF THE CONDITIONS WERE FULFILLED
    else:
        left = False
        right = False
        walkCount = 0


# STEP 1: WE'LL DELETE THE ABILITY TO GO UP AND DOWN
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    #  STEP 4: CALL FUNCTION THAT CREATES THE GAME WINDOW
    windowImage()


pygame.quit()
