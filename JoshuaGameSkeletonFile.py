#+JMJ+AMDG+TTM+

import pygame
from pygame.locals import
from pygame import mixer
import os
import sys
pygame.init()

#information on structuring a game from https://opensource.com/article/17/12/game-framework-python
# Variables
mixer.init()
mixer.music.load('Music File/bensound-summer_wav_music.wav')
mixer.music.play()

worldx = 960
worldy = 720
fps = 40 #frame rate
ani = 4 #animation cycles
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
game_running = True
background = pygame.image.load("SampleBackgroundNotMine.png").convert()

#Objects


#Setup
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

#Main Loop
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                game_running = False

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
