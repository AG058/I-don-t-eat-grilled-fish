import sys , pygame
from pygame.locals import *
from materials import *

game_menu = True
start_game = False

clock = pygame.time.Clock()

while True:
    # 延迟
    delay = 100
    while game_menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 判断开始游戏按钮是否被按下
            if event.type == MOUSEBUTTONDOWN:
                temp = start_game_button.is_or_not_press()
                if temp :
                    start_game = True
                    game_menu = False
                    break
                
        # 绘制背景
        # screen.blit(game_menu_background_image , game_menu_background_image_rect)
        screen.fill((255 , 255 , 255))
        
        # 绘制界面文字按钮
        start_game_button.is_or_not_in_and_blit(screen)

        # 更新屏幕
        pygame.display.update()
        clock.tick(10)

    # 开始游戏
    while start_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 绘制背景
        # screen.blit(start_game_background_image , start_game_background_image_rect)
        screen.fill((255 , 255 , 255))

        # 判断是否碰撞
        player_food_collide = pygame.sprite.spritecollide(player , food_group , False , pygame.sprite.collide_mask)
        if player_food_collide:
            for each in player_food_collide:
                player.inflamed_value += each.inflamed_value
                player.mood_walue += each.mood_walue
                player.nutritional_value += each.nutritional_value

                player.check_value()
                each.reset()
        # 绘制玩家
        player.check()  # 检查边缘
        screen.blit(player.image , player.rect)

        # 绘制食物
        for each in food_group:
            each.move()
            screen.blit(each.image , each.rect)

        
        # 绘制上火条
        inflamed_value_bar_text = status_bar_font.render('上火' , True , BLACK)
        inflamed_value_bar_text_rect = inflamed_value_bar_text.get_rect()
        inflamed_value_bar_text_rect.center = (screen_size_width / 10 , 582)
        screen.blit(inflamed_value_bar_text ,  inflamed_value_bar_text_rect)
        pygame.draw.rect(screen , BLACK , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top + 2 , 100 , inflamed_value_bar_text_rect.height -4  ) , 1)
        
       
        # 更新屏幕
        pygame.display.update()
        clock.tick(60)
