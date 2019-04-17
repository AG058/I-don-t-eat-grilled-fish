import pygame

class Loser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # 初始化显示第一张图
        self.num = 0
        self.image_name = 'images/loser/' + str(self.num) +'.png'
        self.image = pygame.image.load(self.image_name).convert_alpha()
        self.rect = self.image.get_rect()
        

    def update(self):
        if self.num < 10 :
            self.num += 1
        else:
            self.num = 0
        self.update_image()

    # 更新图像
    def update_image(self):
        self.image_name = 'images/loser/' + str(self.num) +'.png'
        self.image = pygame.image.load(self.image_name).convert_alpha()
            
