import pygame
import random

# init pygame
pygame.init()

screenX = 800
screenY = 600
spaceship_x = 32
spaceship_y = 32
enemy_sizeX = 32

# create screen add (()) double pran
screen = pygame.display.set_mode((screenX, screenY))

# Title and Icon customization
pygame.display.set_caption("Arsham")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player vars
player_img = pygame.image.load('spaceship.png')
# X and Y axis to position : Y in upside down
playerX = 370
playerY = 480
playerX_change = 0

# enemy vars
enemy_img = pygame.image.load('ghost.png')
# X and Y axis to position : Y in upside down
enemyX = random.randint(0,screenX)
enemyY = random.randint(50,150)
enemyX_change = 0.5
enemyY_change = 40

# Bullet vars
bullet_img = pygame.image.load('bullet.png')
# X and Y axis to position : Y in upside down
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2

# state is either ready (can't see the bullet) or fired (can see the bullet)
bullet_state = "Ready" 

# PLAYER
def player(x,y):
    # draw the player icon. blit = draw
    screen.blit(player_img, (x,y))

# PLAYER
def enemy(x,y):
    # draw the player icon. blit = draw
    screen.blit(enemy_img, (x,y))

def fire_bullet(x,y):
    # Shoot the bullet
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_img, (x+5,y))

running = True
# Game loop , infinit loop
while running:
    # in RGB values
    screen.fill((229,255,204))

    for event in pygame.event.get():
        # if user quits it
        if event.type == pygame.QUIT:
            running = False

    # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("Keystroke registered")
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # draw the player
    playerX += playerX_change
    # To keep the spaceships within the boundry! 
    # screen width - spaceship width because of 0,0 of spaceship is on the left botom
    if playerX <= 0 : playerX = 0 
    elif playerX >= screenX-spaceship_x : playerX = screenX-spaceship_x


    # Enemy's movement
    enemyX += enemyX_change
    if enemyX <= 0 : 
        enemyX_change = 1
        enemyY += enemyY_change

    elif enemyX >= screenX-enemy_sizeX: 
        enemyX_change = -1
        enemyY += enemyY_change


    # bullet movement
    if bulletY <= 0:
        bullet_state = "Ready"
        bulletY = 480
        

    if bullet_state is "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    # necessary line to update, add everytime
    pygame.display.update()
