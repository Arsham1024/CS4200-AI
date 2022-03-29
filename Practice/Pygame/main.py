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
player_x = 370
player_y = 480

# PLAYER
def player():
    # draw the player icon. blit = draw
    screen.blit(player_img, (player_x,player_y))


running = True
# Game loop , infinit loop
while running:
    # in RGB values
    screen.fill((229,255,204))
    # draw the player
    player()

    for event in pygame.event.get():
        # if user quits it
        if event.type == pygame.QUIT:
            running = False
    
    
    # necessary line to update, add everytime
    pygame.display.update()
