import pygame
from random import  *

class Food_v1(pygame.sprite.Sprite):
    def __init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score ):
        pygame.sprite.Sprite.__init__(self)

        self.before_image = pygame.image.load(food_image).convert_alpha() # 导入图片
        self.image = pygame.transform.smoothscale(self.before_image,(30,30)) # 缩小图片
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image) # 创建遮罩，检测碰撞用

        # 初始化速度，上火值，心情值，营养值，分数
        self.speed = 4
        self.inflamed_value = inflamed_value
        self.mood_value = mood_value
        self.nutritional_value = nutritional_value
        self.score = score

        # 保存活动范围大小
        self.active_size = active_size

        # 初始化位置
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0] , self.active_size[0] * 8)

        # 初始化半径
        self.radius = self.rect.width // 2

        # 当用户按下暂停键时的速度
        self.pause_speed = 0
        self.unpause_speed = self.speed

    # 移动
    def move(self):
        self.rect.left -= self.speed
        if self.rect.right <= 0:
            self.reset()

    # 重新初始化位置 
    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0] , self.active_size[0] * 8)

class Food_v2(Food_v1):
    def __init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score ):
        Food_v1.__init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score )

        # 初始化位置
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 18 )

        # 初始化速度
        self.speed = 3
        
    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]  , self.active_size[0] * 18)

class Food_v3(Food_v1):
    def __init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score ):
        Food_v1.__init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score )

        # 初始化位置
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 30)

        # 初始化速度
        self.speed = 3
        
    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 30)

class Food_v4(Food_v1):
    def __init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score ):
        Food_v1.__init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score )

        # 初始化位置
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 40)

        # 初始化速度
        self.speed = 2
        
    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 40)

class Food_v5(Food_v1):
    def __init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score ):
        Food_v1.__init__(self , active_size , food_image , inflamed_value , mood_value , nutritional_value , score )

        # 初始化位置
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 60)

        # 初始化速度
        self.speed = 2
        
    def reset(self):
        self.rect.top = randint(10 , self.active_size[1] -20 )
        self.rect.left = randint( self.active_size[0]   , self.active_size[0] * 60)
