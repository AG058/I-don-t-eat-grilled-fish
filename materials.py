import pygame
from pygame.locals import *
from button import *
from food import *
from player import *
from random import *

# 初始化
pygame.init()
pygame.mixer.init()

# 定义屏幕大小
screen_size = screen_size_width , screen_size_height = 800 , 600
screen_size_center = screen_size_width // 2 , screen_size_height // 2
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('游戏标题')

# 定义游戏活动大小
screen_active_size = 800 , 550

# 定义颜色
BLACK = 0 , 0 , 0
GRAY_0 = 50 , 50 ,50
GRAY_1 = 150,150,150
GRAY_2 = 170 , 170 , 170
GREEN = 0 , 255 , 0
RED = 255 , 0 , 0
status_bar_font_color = BLACK

# 导入图片
game_menu_background_image = pygame.image.load('images/game_menu_background.jpg')
game_menu_background_image_rect = game_menu_background_image.get_rect()
start_game_background_image = pygame.image.load('images/start_game_background.png')
start_game_background_image_rect = start_game_background_image.get_rect()

# 定义字体
food_font = pygame.font.Font('font/font.ttf' , 20)
button_font = pygame.font.Font('font/font.ttf' , 40)
status_bar_font = pygame.font.Font('font/font.ttf' , 15)
target_font = pygame.font.Font('font/font.ttf' , 20)

# 定义游戏界面按钮
start_game_button = TextButton(button_font ,' 开  始  游  戏' , BLACK , GRAY_1 , (400 , 500) )

# 水果速度
fruit_speed = 3
# 食物名称，速度，上火值，心情值，营养值，分数
food_v1_path = 'images/food/v1/'
food_v1 = [ [food_v1_path+'apple.png',fruit_speed,-2,5,5,3] ,
            [food_v1_path+'milk.png',3,3,10,5,4],
           [food_v1_path+'rice.png' , 3 , -3 , 5, 10 , 3] ,
            [food_v1_path+'pear.png',fruit_speed,-5,5,5,3],
           [food_v1_path+'rice_ball.png' , fruit_speed , -3 , 7 , 10 , 3]]
food_v2_path = 'images/food/v2/'
food_v2 = [ [food_v2_path + 'bagel.png' , 4 , 8 , 20 , 15 , 8] ,
            [food_v2_path + 'bread.png' , 4 , 8 , 15 , 10 , 8] ,
            [food_v2_path + 'chocolate.png' , 3 , 10 , 20 , 10 , 10],
            [food_v2_path + 'lollipop.png' , 4 , 5 , 10 , 5 , 6] ,
            [food_v2_path + 'meat-on-bone.png' , 3 ,3 , 20 , 25 , 12],
            [food_v2_path + 'watermelon.png' , 3 , -5 , 15 , 5 ,3]]
food_v3_path = 'images/food/v3/'




# 自定义事件：心情值，营养值随时间每一秒减少
TIME = USEREVENT
pygame.time.set_timer(TIME , 1 * 1000)

# 目标时间以及目标分数
targets = {1:[30,25] ,
           2:[30,125]}

# 导入玩家
player = Player('images/player.png',screen_active_size)

# 创建食物组
food_group = pygame.sprite.Group()

# 创建初始v1食物，每种4个
for food_name , food_speed , food_inflamed_value , food_mood_value , food_nutritional_value , food_score \
              in food_v1 :
    for i in range(4):
        food = Food_v1(screen_active_size ,  \
                           food_name , food_speed , food_inflamed_value , \
                           food_mood_value , food_nutritional_value , food_score )
        food_group.add(food)

# 初始化级别
food_level = 1
target_level = 1
