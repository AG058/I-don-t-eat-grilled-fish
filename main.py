import sys , pygame
from pygame.locals import *
from materials import *

game_menu = True
start_game = False
game_over = False

clock = pygame.time.Clock()

while True:
    # 延迟
    delay = 100
    # 游戏进入界面
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
    # 初始化目标计时器，目标分数
    target_time ,  target_score= targets[level][0] , targets[level][1]
    while start_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 心情值，营养值随每秒减少，倒计时减少
            if event.type == TIME:
                player.mood_value -= 2
                player.nutritional_value -= 3
                target_time -= 1
                if target_time <= 0 : # 倒计时结束
                    if player.score >= target_score : # 玩家分数达到目标分数
                        next_level = True # 下一关界面开启
                        start_game = False
                    else :
                        game_over_because_score = True # 记录由于分数未达到导致失败
                        game_over = True
                        start_game = False
                
        # 绘制背景
        screen.blit(start_game_background_image , start_game_background_image_rect)

        # 判断是否碰撞
        player_food_collide = pygame.sprite.spritecollide(player , food_group , False , pygame.sprite.collide_circle)
        if player_food_collide:
            for each in player_food_collide:
                player.inflamed_value += each.inflamed_value
                player.mood_value += each.mood_value
                player.nutritional_value += each.nutritional_value
                player.score += each.score

                # 检测三个值是否满足游戏失败值
                player.check_value()
                if player.inflamed_value_status or player.mood_value_status or player.nutritional_value_status:
                    game_over = True
                    start_game = False
                    break
                
                each.reset()
                
        # 绘制玩家
        player.check()  # 检查边缘
        screen.blit(player.image , player.rect)

        # 绘制食物
        for each in food_group:
            each.move()
            screen.blit(each.image , each.rect)

        
        # 绘制上火条 ， 以下代码是找适当的位置放条
        # 绘制”上火“
        inflamed_value_bar_text = status_bar_font.render('上火' , True , status_bar_font_color)
        inflamed_value_bar_text_rect = inflamed_value_bar_text.get_rect()
        inflamed_value_bar_text_rect.center = (screen_size_width / 18 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(inflamed_value_bar_text ,  inflamed_value_bar_text_rect)
        # 绘制血条
        if player.inflamed_value < 80 :
            pygame.draw.rect(screen , GREEN , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , player.inflamed_value , inflamed_value_bar_text_rect.height   ) )
        elif 80 <= player.inflamed_value <= 100 :
            pygame.draw.rect(screen , RED , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , player.inflamed_value , inflamed_value_bar_text_rect.height   ) )
        r_i = pygame.draw.rect(screen , status_bar_font_color , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , 100 , inflamed_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字     
        inflamed_value_bar_num_text = status_bar_font.render(str(player.inflamed_value), True , status_bar_font_color)
        inflamed_value_bar_num_text_rect = inflamed_value_bar_num_text.get_rect()
        inflamed_value_bar_num_text_rect.topleft =  r_i.right + 2 , inflamed_value_bar_text_rect.top 
        screen.blit(inflamed_value_bar_num_text , inflamed_value_bar_num_text_rect)

        
        # 绘制心情条
        # 绘制”心情“
        mood_value_bar_text = status_bar_font.render('心情' , True , status_bar_font_color)
        mood_value_bar_text_rect = mood_value_bar_text.get_rect()
        mood_value_bar_text_rect.center = (screen_size_width / 18 * 5 +5 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(mood_value_bar_text ,  mood_value_bar_text_rect)
        # 绘制血条
        if player.mood_value < 20 :
            pygame.draw.rect(screen , RED , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , player.mood_value , mood_value_bar_text_rect.height   ) )
        elif 20 <= player.mood_value <= 100 :
            pygame.draw.rect(screen , GREEN , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , player.mood_value , mood_value_bar_text_rect.height   ) )
        r_m = pygame.draw.rect(screen , status_bar_font_color , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , 100 , mood_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字     
        mood_value_bar_num_text = status_bar_font.render(str(player.mood_value), True , status_bar_font_color)
        mood_value_bar_num_text_rect = mood_value_bar_num_text.get_rect()
        mood_value_bar_num_text_rect.topleft =  r_m.right + 2 , mood_value_bar_text_rect.top 
        screen.blit(mood_value_bar_num_text , mood_value_bar_num_text_rect)

        # 绘制营养条
        # 绘制”营养“
        nutritional_value_bar_text = status_bar_font.render('营养' , True , status_bar_font_color)
        nutritional_value_bar_text_rect = nutritional_value_bar_text.get_rect()
        nutritional_value_bar_text_rect.center = (screen_size_width / 18 * 9 +10 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(nutritional_value_bar_text ,  nutritional_value_bar_text_rect)
        # 绘制血条
        if player.nutritional_value < 20 :
            pygame.draw.rect(screen , RED , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , player.nutritional_value , nutritional_value_bar_text_rect.height   ) )
        elif 20 <= player.nutritional_value<= 100 :
            pygame.draw.rect(screen , GREEN , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , player.nutritional_value , nutritional_value_bar_text_rect.height   ) )
        r_n = pygame.draw.rect(screen , status_bar_font_color , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , 100 , nutritional_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字     
        nutritional_value_bar_num_text = status_bar_font.render(str(player.nutritional_value), True , status_bar_font_color)
        nutritional_value_bar_num_text_rect = nutritional_value_bar_num_text.get_rect()
        nutritional_value_bar_num_text_rect.topleft =  r_n.right + 2 , nutritional_value_bar_text_rect.top 
        screen.blit(nutritional_value_bar_num_text , nutritional_value_bar_num_text_rect)

        # 绘制分数条
        score_text = status_bar_font.render('分数：'+str(player.score) , True , status_bar_font_color)
        screen.blit(score_text , (screen_size_width / 18 * 13 + 10, nutritional_value_bar_text_rect.top ))

        # 绘制目标分数，倒计时
        target_text = target_font.render('目标分数：%d  倒计时：%d' % (target_score , target_time) , True , status_bar_font_color)
        target_text_rect = target_text.get_rect()
        target_text_rect.topleft= screen_size_width - target_text_rect.width  , 10
        screen.blit(target_text , target_text_rect)
        
        # 判断分数是否达到下一等级
        if player.score >= 25and level == 1:
            level = 2
            # 创建初始v2食物，每种3个
            for food_name , food_speed , food_inflamed_value , food_mood_value , food_nutritional_value , food_score \
                          in food_v2 :
                for i in range(3):
                    food = Food_v1(screen_active_size ,  \
                                       food_name , food_speed , food_inflamed_value , \
                                       food_mood_value , food_nutritional_value , food_score )
                    food_group.add(food)

        # 更新屏幕
        pygame.display.update()
        clock.tick(30)
