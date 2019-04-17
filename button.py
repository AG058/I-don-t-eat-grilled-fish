import pygame

# 文字按钮
class TextButton(pygame.sprite.Sprite):
    def __init__(self , font , text , unpress_color , press_color ):
        pygame.sprite.Sprite.__init__(self)
        
        self.unpress = font.render(text , True , unpress_color)
        self.press = font.render(text , True , press_color)
        self.rect = self.unpress.get_rect()
        # 是否被按下
        self.state = False

    # 判断鼠标位置是否在按钮上，并且绘制相应按钮样式
    def is_or_not_in_and_blit(self ,screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.press , self.rect)
            self.state = True
        else :
            screen.blit(self.unpress , self.rect)
            self.state = False

    # 判断鼠标是否在按钮上，返回是或否
    def is_or_not_press(self):
        if self.state:
            return True
        else :
            return False
