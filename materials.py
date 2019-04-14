import pygame , sys
from pygame.locals import *
from button import *
from food import *
from player import *
from random import *
from loser import *
from defeat_beacuse_text_image import *
    
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

# 定义 icon
icon_image = pygame.image.load('images/ico .ico').convert_alpha()
pygame.display.set_icon(icon_image)

# 定义颜色
BLACK = 0 , 0 , 0
GRAY_0 = 50 , 50 ,50
GRAY_1 = 150,150,150
GRAY_2 = 170 , 170 , 170
GREEN = 0 , 255 , 0
RED = 255 , 0 , 0
GRAY_3 = 100 , 100 , 100
status_bar_font_color = BLACK
next_target_font_color = BLACK


# 导入图片
game_menu_background_image = pygame.image.load('images/game_menu_background.jpg')
game_menu_background_image_rect = game_menu_background_image.get_rect()
start_game_background_image = pygame.image.load('images/start_game_background.png').convert_alpha()
start_game_background_image_rect = start_game_background_image.get_rect()
copy_little_image = start_game_background_image .subsurface(740,550,60,50) # 用于填补右下角暂停按钮的背景
copy_little_image_rect = copy_little_image.get_rect()
copy_little_image_rect.bottomright = screen_size_width , screen_size_height
text_background_image = pygame.image.load('images/text_background.png').convert_alpha()
text_background_image_rect = text_background_image.get_rect()
text_background_image_rect.center = start_game_background_image_rect.center
space_text_image = pygame.image.load('images/space.png').convert_alpha()
space_text_image_rect = space_text_image.get_rect()
unpause_button_image = pygame.image.load('images/unpause_button.png').convert_alpha()
pause_button_image = pygame.image.load('images/pause_button.png').convert_alpha()
unpause_and_pause_button_image_rect = unpause_button_image.get_rect()
defeat_image = pygame.image.load('images/defeat.png').convert_alpha()
defeat_image_rect = defeat_image.get_rect()
defeat_image_rect.centerx = screen_size_width // 2
defeat_image_rect.top = screen_size_height // 12
defeat_bg_image = pygame.image.load('images/defeat_bg.png').convert_alpha()
defeat_bg_image_rect = defeat_bg_image.get_rect()

# 创建失败者loser类
loser = Loser()
loser.rect.centerx = screen_size_width // 2
loser.rect.top = screen_size_height //12* 2 -10

# 创建失败原因文字图片类
defeat_beacuse_text = Defeat_Beacuse_Text_Image(screen_size_width , loser.rect.bottom)

# 定义字体
font_40 = pygame.font.Font('font/font.ttf' , 40)
font_15 = pygame.font.Font('font/font.ttf' , 15)
font_20 = pygame.font.Font('font/font.ttf' , 20)
font_55 =  pygame.font.Font('font/font.ttf' , 55)
font_35 = pygame.font.Font('font/font.ttf' , 35)
font_90 = pygame.font.Font('font/font.ttf' , 90)

# 定义游戏界面按钮
start_game_button = TextButton(font_40 ,' 开  始  游  戏' , BLACK , GRAY_1 )
start_game_button.rect.center = (400 , 500)
# 定义游戏结束界面返回菜单和重新开始按钮
return_menu_button = TextButton(font_40 ,' 返回菜单'  , BLACK ,  GRAY_0)
restart_button = TextButton(font_40 ,' 重新开始' , BLACK,  GRAY_0 )

# 食物名称，上火值，心情值，营养值，分数
food_v1_path = 'images/food/v1/'
food_v1 = [ [food_v1_path+'apple.png',-2,5,5,3] ,
            [food_v1_path+'milk.png',3,10,5,4],
           [food_v1_path+'rice.png' , -3 , 5, 10 , 3] ,
            [food_v1_path+'pear.png',-5,5,5,3],
           [food_v1_path+'rice_ball.png' , -3 , 7 , 10 , 3]]
food_v2_path = 'images/food/v2/'
food_v2 = [ [food_v2_path + 'bagel.png' , 8 , 20 , 15 , 8] ,
            [food_v2_path + 'bread.png' , 8 , 15 , 10 , 8] ,
            [food_v2_path + 'chocolate.png' , 10 , 20 , 10 , 10],
            [food_v2_path + 'lollipop.png', 5 , 10 , 5 , 6] ,
            [food_v2_path + 'meat-on-bone.png' ,3 , 20 , 25 , 12],
            [food_v2_path + 'watermelon.png' ,-5 , 15 , 5 ,3]]
food_v3_path = 'images/food/v3/'


# 自定义事件：心情值，营养值随时间每一秒减少
TIME = USEREVENT
pygame.time.set_timer(TIME , 1 * 1000)
# 自定义事件：每过0.01秒更新loser图片
UPDATE_LOSER_TIME = USEREVENT + 1
pygame.time.set_timer(UPDATE_LOSER_TIME ,  10)

# 目标时间以及目标分数
targets = {1:[30,25] ,
           2:[40,125]}





