# STARTING PYGAME(HIT BOX AND COLLISIONS)

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game')


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

# STEP 3. CREATE SCORE COUNTER
score = 0


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
        self.standing = True

        self.hitbox = (self.x + 17, self.y+11, 31, 57)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y+11, 31, 57)

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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


class Enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load(
        'R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load(
        'L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = (self.x, self.end)
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 21, 40, 50)
        # STEP 7. CREATE HEALTH BAR
        self.health = 9
        # STEP 8. CREATE VISIBLE VARIABLE
        self.visible = True

    def draw(self, win):
        self.move()
        # STEP 9.WRITE STATEMENT TO DRAW CHARACTER IF CHARACTER IS VISIBLE
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            # STEP 6. CREATE RECTANGLE
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            # STEP 10. INCLUDE STATEMENT TO REDUCE HEALTH BAR IF CHARACTER GOBLIN IS HIT
            pygame.draw.rect(win, (0, 200, 0),
                             (self.hitbox[0], self.hitbox[1]-20, 50-(4.85*(9-self.health)), 10))
            self.hitbox = (self.x + 20, self.y, 28, 60)

        # pygame.draw.rect(win, (255, 0, 0), (self.x + 20, self.y, 28, 60), 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        # STEP 9. CREATE VARIABLE FOR IF HEALTH IS 0 OR MORE
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def windowImage():
    win.blit(bg, (0, 0))
    # STEP 4. CREATE TEXT VARIABLE
    text = font.render('score :' + str(score), 1, (255, 0, 0))
    # STEP 5. BLIT THE IMAGE
    win.blit(text, (310, 10))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw_circle(win)

    pygame.display.update()


# STEP 1. CREATE FONT VARIABLE

font = pygame.font.SysFont('comicsans', 20, True, True)
run = True
bullets = []

shootloop = 0
enemy = Enemy(45, 380, 64, 64, 450)
man = Player(45, 360, 64, 64)
while run:
    clock.tick(27)

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:

        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))
                # STEP 2. INCREMENT SCORE COUNTER
                score += 1
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 7:
            bullets.append(Projectile(round(man.x + man.width//2),
                           round(man.y + man.height//2), (255, 0, 0), 5, facing))
        dshootloop = 1

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
