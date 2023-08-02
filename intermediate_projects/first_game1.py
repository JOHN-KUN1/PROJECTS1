# STARTING PYGAME(BASIC MOVEMENTS AND KEY PRESSES)

# STEP 1 IMPORT PYGAME INITIALIZE IT
import pygame
pygame.init()

# STEP 2 CREATE THE PYGAME WINDOW AND SET THE CAPTION
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game')

# STEP 3 CREATE THE OBJECT YOULL BE USING IN THE GAME its x and y position, its width and height AND GIVE IT ITS VELOCITY
x = 50
y = 50
height = 60
width = 60
vel = 15


# STEP 4 CREATE THE MAIN LOOP: 1. CHECK FOR EVENTS 2.DRAW THE CHARACTER 3. CHECK IF KEYS HAS BEEN PRESSED 5. WRITE THE CONDITIONAL STATEMENTS FOR IF UP,LEFT,RIGHT,DOWN KEY HAS BEEN PRESSED 6. FILL THE SCREEN
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
