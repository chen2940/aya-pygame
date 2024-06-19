import pygame
from pygame.sprite import Sprite


class Baseitem(Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
