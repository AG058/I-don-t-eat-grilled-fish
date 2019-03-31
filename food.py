import pygame
from random import  *

class FoodText_v1(pygame.sprite.Sprite):
    def __init__(self , active_size , font , font_color , text , speed , inflamed_value , mood_walue , nutritional_value , score ):
        pygame.sprite.Sprite.__init__(self)

        self.image = font.render(text , True , font_color)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.speed = speed
        self.inflamed_value = inflamed_value
        self.mood_walue = mood_walue
        self.nutritional_value = nutritional_value
        self.score = score

        self.active_size = active_size

    def move(self):
        self.rect.left -= self.speed
        if self.rect.right <= 0:
            self.reset()

    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -5 )
        self.rect.left = randint( self.active_size[0] , self.active_size[0] * 5)
