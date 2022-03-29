import pygame

# init pygame
pygame.init()

# create screen add (()) double pran
screen = pygame.display.set_mode((800, 600))

running = True
# Game loop , infinit loop
while running:
    for event in pygame.event.get():
        # if user quits it
        if event.type == pygame.QUIT:
            running = False
    

