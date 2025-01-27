import random
import pygame

pipe_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
TILE_SIZE = 50


class Pipe(pygame.sprite.Sprite):
    def __init__(self, pipes, all_sprites):
        super().__init__(pipes, all_sprites)
        self.rotation = random.randint(0, 3)
        self.has_water = False

    def check_for_water(self):
        pass


class IPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(pipe_sprites, all_sprites)
        if self.rotation % 2 == 1:
            self.image = pygame.image.load('data/pipe_straight_90.png')
        else:
            self.image = pygame.image.load('data/pipe_straight_0.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class LPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(pipe_sprites, all_sprites)
        if self.rotation == 0:
            self.image = pygame.image.load('data/pipe_corner_0.png')
        elif self.rotation == 1:
            self.image = pygame.image.load('data/pipe_corner_90.png')
        elif self.rotation == 2:
            self.image = pygame.image.load('data/pipe_corner_180.png')
        else:
            self.image = pygame.image.load('data/pipe_corner_270.png')
        self.rect = self.image.get_rect()
