import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self , filename , active_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.active_size = active_size

        
    def check(self):
        self.rect.center = pygame.mouse.get_pos()
        if self.rect.left != 0 :
            self.rect.left = 0
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom >= self.active_size[1] + 15:
            self.rect.bottom = self.active_size[1] +15
