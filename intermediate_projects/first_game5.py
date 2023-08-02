# STARTING PYGAME(PROJECTILES)

import pygame
pygame.init()

win = pygame.display.set_mode((500, 450))
pygame.display.set_caption('My First Game')


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        # STEP 3. CREATE A STANDING ATTRIBUTE
        self.standing = True

    def draw(self, win):
        # STEP 4. WRITE A STATEMENT TO CHECK IF THE PLAYER IS STANDING OR NOT
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
# STEP 2. WRITE AN ELSE STATEMENT THAT DRAWS AN IMAGE IF THE PLAYER IS WALKING RIGHT OR LEFT
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

# STEP 1. 1. CREATE A CLASS THAT HAS ATTRIBUTES OF  X , Y ,RADIUS, COLOR, FACING 2. CREATE A DRAW METHOD TO DRAW A CIRCLE IN PYGAME


class Projectile(object):
    def __init__(self, x, y, color, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw_circle(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def windowImage():
    win.blit(bg, (0, 0))
    man.draw(win)
# STEP 7. WRITE A STATEMETNT TO DRAW EACH BULLET
    for bullet in bullets:
        bullet.draw_circle(win)
    pygame.display.update()


run = True
bullets = []
man = Player(45, 360, 64, 64)
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


# STEP 6. CREATE A NEW FOR LOOP FOR THE BULLETS: 1. WRITE A STATEMENT IF SPACE IS BEING PRESSED TO SHOOT
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 7:
            bullets.append(Projectile(round(man.x + man.width//2),
                           round(man.y + man.height//2), (255, 0, 0), 5, facing))


# STEP 5. CHECK IF PLAYER IS WALKING OR NOT
    if keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    windowImage()


pygame.quit()
