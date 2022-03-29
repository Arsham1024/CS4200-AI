import pygame

# init pygame
pygame.init()

# create screen add (()) double pran
screen = pygame.display.set_mode((800, 600))

# Title and Icon customization
pygame.display.set_caption("Arsham")
icon = pygame.image.load('face-recognition.png')
pygame.display.set_icon(icon)

# Player vars
player_img = pygame.image.load('letter-a.png')
# X and Y axis to position : Y in upside down
playerX = 370
playerY = 480
playerX_change = 0

# PLAYER
def player(x,y):
    # draw the player icon. blit = draw
    screen.blit(player_img, (x,y))


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
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # draw the player
    playerX += playerX_change
    player(playerX,playerY)
    # necessary line to update, add everytime
    pygame.display.update()
