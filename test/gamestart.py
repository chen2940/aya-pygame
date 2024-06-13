# Example file showing a circle moving on screen
import random

import pygame, sys

# pygame setup
pygame.init()

size = chang, kuan = 600, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# pygame.display.set_icon("")
pygame.display.set_caption("ball")
speed = [1, 1]
BLACK = 0, 0, 0
ball = pygame.image.load("ball.jpg")
fps = 120
ballrect = ball.get_rect()
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ballrect.move(10, 0)
        if keys[pygame.K_DOWN]:
            ballrect.move(-10, 0)
        if keys[pygame.K_ESCAPE]:
            sys.exit()
    # ballrect = ballrect.move(speed[0], speed[1])
    # if ballrect.left < 0 or ballrect.right > chang:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > kuan:
    #     speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
