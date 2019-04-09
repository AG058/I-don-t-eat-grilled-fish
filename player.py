import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self , filename , active_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.active_size = active_size

        # 初始化上火值，心情值，营养值，分数
        self.inflamed_value = 0
        self.mood_value = 100
        self.nutritional_value = 100
        self.score = 0

        # 初始化半径
        self.radius = 7

        # 三个值状态
        self.inflamed_value_status = False
        self.mood_value_status = False
        self.nutritional_value_status = False
        
    # 边缘检测 
    def check(self):
        self.rect.center = pygame.mouse.get_pos()
        if self.rect.left != 0 :
            self.rect.left = 0
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom >= self.active_size[1] + 15:
            self.rect.bottom = self.active_size[1] +15

    # 检测三个值是否满足游戏失败值，并进行边缘检测
    def check_value(self):
        if self.inflamed_value <= 0 :
            self.inflamed_value = 0
        if self.inflamed_value >= 100 :
            self.inflamed_value = 100
            self.inflamed_value_status = True
        if self.mood_value <= 0 :
            self.mood_value = 0
            self.mood_value_status = True
        if self.mood_value >= 100 :
            self.mood_value = 100
        if self.nutritional_value <= 0 :
            self.nutritional_value = 0
            self.nutritional_value_status = True
        if self.nutritional_value >= 100 :
            self.nutritional_value = 100
            
    
    
