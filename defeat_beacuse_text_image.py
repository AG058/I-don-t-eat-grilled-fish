import pygame

class Defeat_Beacuse_Text_Image(pygame.sprite.Sprite):
    def __init__(self , screen_size_width , loser_rect_bottom):
        pygame.sprite.Sprite.__init__(self )

        self.defeat_score_image_name = 'images/defeat_score.png' # 由于分数不够失败
        self.defeat_3_true_image_name = 'images/3-true.png' # 由于上火值心情值营养值同时失败
        self.defeat_2_true_1_image_name = 'images/2-true-1.png' # 由于上火值心情值失败
        self.defeat_2_true_2_image_name = 'images/2-true-2.png' # 由于上火值营养值失败
        self.defeat_2_true_3_image_name = 'images/2-true-3.png' # 由于心情值营养值失败
        self.defeat_1_true_1_image_name = 'images/1-true-1.png' # 由于上火值失败
        self.defeat_1_true_2_image_name = 'images/1-true-2.png' # 由于心情值失败
        self.defeat_1_true_3_image_name = 'images/1-true-3.png' # 由于营养值失败

        self.screen_size_width = screen_size_width 
        self.loser_rect_bottom = loser_rect_bottom

    # 传入分数是否失败，上火值是否失败，心情值是否失败，营养值是否失败
    def check(self , b0 ,b1 , b2 , b3 ):
        if b0: 
            self.image = pygame.image.load(self.defeat_score_image_name).convert_alpha()
        if b1 and b2 and b3:
            self.image = pygame.image.load(self.defeat_3_true_image_name).convert_alpha()
        if b1 and b2 :
            self.image = pygame.image.load(self.defeat_2_true_1_image_name).convert_alpha()
        if b1 and b3 :
            self.image = pygame.image.load(self.defeat_2_true_2_image_name).convert_alpha()
        if b2 and b3 :
            self.image = pygame.image.load(self.defeat_2_true_3_image_name).convert_alpha()
        if b1 :
            self.image = pygame.image.load(self.defeat_1_true_1_image_name).convert_alpha()
        if b2 :
            self.image = pygame.image.load(self.defeat_1_true_2_image_name).convert_alpha()
        if b3 :
            self.image = pygame.image.load(self.defeat_1_true_3_image_name).convert_alpha()

        # 位置在失败者动图下方
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_size_width // 2
        self.rect.top = self.loser_rect_bottom +10
