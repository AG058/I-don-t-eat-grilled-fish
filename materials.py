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
start_game_background_image = pygame.image.load('images/start_game_background.jpg')
start_game_background_image_rect = start_game_background_image.get_rect()

# 定义字体
food_font = pygame.font.Font('font/font.ttf' , 20)
button_font = pygame.font.Font('font/font.ttf' , 40)
status_bar_font = pygame.font.Font('font/font.ttf' , 15)

# 定义游戏界面按钮
start_game_button = TextButton(button_font ,' 开  始  游  戏' , BLACK , GRAY_1 , (400 , 500) )

# 水果速度
fruit_speed = 3
# 食物名称，速度，上火值，心情值，营养值，分数
food_v1_path = 'images/food/v1/'
food_v1= [ [food_v1_path+'apple.png',fruit_speed,-2,5,5,10] , [food_v1_path+'milk.png',3,3,10,5,10],
           [food_v1_path+'rice.png' , 3 , 0 , 5, 10 , 10] , [food_v1_path+'pear.png',fruit_speed,-5,5,5,10],
           [food_v1_path+'rice_ball.png' , fruit_speed , 0 , 7 , 10 , 15]]
food_v3 = [['烤鱼',1,50,50,80,3]]

# 自定义事件：心情值，营养值随时间每一秒减少
REDUCE_VALUE = USEREVENT
pygame.time.set_timer(REDUCE_VALUE , 1 * 1000)

# 导入玩家
player = Player('images/player.png',screen_active_size)

# 创建食物组
food_group = pygame.sprite.Group()

# 创建初始v1食物，每种5个
for food_name , food_speed , food_inflamed_value , food_mood_value , food_nutritional_value , food_score \
              in food_v1 :
    for i in range(5):
        food = FoodText_v1(screen_active_size ,  \
                           food_name , food_speed , food_inflamed_value , \
                           food_mood_value , food_nutritional_value , food_score )
        food_group.add(food)
