import pygame
from materials import *

class TextButton(pygame.sprite.Sprite):
    def __init__(self , font , text , unpress_color , press_color , position):
        pygame.sprite.Sprite.__init__(self)
        
        self.unpress = font.render(text , True , unpress_color)
        self.press = font.render(text , True , press_color)
        self.rect = self.unpress.get_rect()
        self.rect.center = position
        self.state = False

    def is_or_not_in_and_blit(self ,screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.press , self.rect)
            self.state = True
        else :
            screen.blit(self.unpress , self.rect)
            self.state = False

    def is_or_not_press(self):
        if self.state:
            return True
        else :
            return False
