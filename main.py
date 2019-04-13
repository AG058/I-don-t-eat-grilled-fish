from materials import *

game_menu = True
start_game = False
game_over = False
game_over_because_score = False # 录由于分数未达到导致失败
next_level = False  # 下一关界面开启
pause_status = False # 初始化暂停为false
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
                    next_level = True
                    game_menu = False
                    break
                
        # 绘制背景
        # screen.blit(game_menu_background_image , game_menu_background_image_rect)
        screen.fill((255 , 255 , 255))
        
        # 绘制界面文字按钮
        start_game_button.is_or_not_in_and_blit(screen)

        # 更新屏幕
        pygame.display.flip()
        clock.tick(10)

    
    # 初始化目标计时器，目标分数
    target_time ,  target_score= targets[target_level][0] , targets[target_level][1]
    # 下一关开启界面只持续5秒钟，显示“恭喜通关”时间3秒，显示关卡信息3秒
    if target_level == 1:
        next_time = 3
    else :
        next_time = 0
    # 下一关开启界面
    while next_level:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 判断暂停
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pause_status = not pause_status
                    
            # 显示时间是否足够3秒
            if event.type == TIME:
                if pause_status == False :
                    if next_time  == 5:
                        start_game = True
                        next_level = False
                    else:
                        next_time += 1

        # 绘制背景
        if target_level == 1:
            screen.blit(start_game_background_image , start_game_background_image_rect)
        
        
        # 绘制文字背景框
        screen.blit(text_background_image , text_background_image_rect)

        # 绘制“恭喜通关”，并显示2秒后显示关卡信息
        if target_level > 1 and (next_time  <= 2):
            next_message_text = font_90.render('恭喜通关' , True , next_target_font_color)
            next_message_text_rect = next_message_text.get_rect()
            next_message_text_rect.center = text_background_image_rect.center
            screen.blit(next_message_text , next_message_text_rect)
        elif next_time  > 2:
            # 绘制文字背景框
            screen.blit(text_background_image , text_background_image_rect)
            
            # 绘制关卡提示文字
            next_target_text = font_55.render('第 %d 关' % target_level , True , next_target_font_color)
            next_target_text_rect = next_target_text.get_rect()
            next_target_text_rect.center = text_background_image_rect.center[0] , \
                                           text_background_image_rect.top + text_background_image_rect.height // 3
            screen.blit(next_target_text , next_target_text_rect)
            next_target_time_text = font_35.render('时间：%d' % (target_time ) , True , next_target_font_color)
            next_target_time_text_rect = next_target_time_text.get_rect()
            next_target_time_text_rect.center = text_background_image_rect.center[0] , \
                                           text_background_image_rect.top + text_background_image_rect.height // 5 * 3
            screen.blit(next_target_time_text , next_target_time_text_rect)
            next_target_score_text = font_35.render('分数：%d' % (target_score ) , True , next_target_font_color)
            next_target_score_text_rect = next_target_score_text.get_rect()
            next_target_score_text_rect.center = text_background_image_rect.center[0] , \
                                           text_background_image_rect.top + text_background_image_rect.height // 5 * 4
            screen.blit(next_target_score_text , next_target_score_text_rect)
        
        # 绘制按钮地区的背景，防止按钮重叠
        screen.blit(copy_little_image , copy_little_image_rect)
        
        # 绘制开始暂停按钮,空格文字图片
        unpause_and_pause_button_image_rect.centery = screen_size_height - \
                                                      (screen_size_height - screen_active_size[1]) // 2
        unpause_and_pause_button_image_rect.right = screen_size_width - 10
        space_text_image_rect.right = unpause_and_pause_button_image_rect.left
        space_text_image_rect.top = unpause_and_pause_button_image_rect.top
        screen.blit(space_text_image , space_text_image_rect)
        if pause_status :
            screen.blit(pause_button_image , unpause_and_pause_button_image_rect)
        else :
            screen.blit(unpause_button_image , unpause_and_pause_button_image_rect)
            
        # 更新屏幕
        pygame.display.update()
        clock.tick(10)
        
    # 开始游戏
    while start_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 用户按下空格键暂停游戏
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pause_status = not pause_status
                    
            # 心情值，营养值随每秒减少，倒计时减少
            if event.type == TIME:
                if pause_status == False:
                    player.mood_value -= 2
                    player.nutritional_value -= 3         
                    target_time -= 1
                    if target_time <= 0 : # 倒计时结束
                        if player.score >= target_score : # 玩家分数达到目标分数
                            next_level = True # 下一关界面开启
                            target_level += 1
                            start_game = False
                        else :
                            game_over_because_score = True # 记录由于分数未达到导致失败
                            game_over = True
                            start_game = False
                
        # 绘制背景
        screen.blit(start_game_background_image , start_game_background_image_rect)
                
        # 绘制玩家
        if pause_status == False:
            player.check()  # 检查边缘
        screen.blit(player.image , player.rect)

        # 绘制食物
        if pause_status == False:
            for each in food_group:
                each.move()
        for each in food_group:
            screen.blit(each.image , each.rect)

        # 判断是否碰撞
        player_food_collide = pygame.sprite.spritecollide(player , food_group , False , pygame.sprite.collide_circle)
        if player_food_collide:
            for each in player_food_collide:
                player.inflamed_value += each.inflamed_value
                player.mood_value += each.mood_value
                player.nutritional_value += each.nutritional_value
                player.score += each.score
                
                each.reset()
                
        # 绘制上火条 ， 以下代码是找适当的位置放条
        # 绘制”上火“
        inflamed_value_bar_text = font_15.render('上火' , True , status_bar_font_color)
        inflamed_value_bar_text_rect = inflamed_value_bar_text.get_rect()
        inflamed_value_bar_text_rect.center = (screen_size_width / 18 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(inflamed_value_bar_text ,  inflamed_value_bar_text_rect)
        # 绘制血条
        if 0 <= player.inflamed_value < 80 :
            pygame.draw.rect(screen , GREEN , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , player.inflamed_value , inflamed_value_bar_text_rect.height   ) )
        elif 80 <= player.inflamed_value <= 100 :
            pygame.draw.rect(screen , RED , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , player.inflamed_value , inflamed_value_bar_text_rect.height   ) )
        r_i = pygame.draw.rect(screen , status_bar_font_color , (inflamed_value_bar_text_rect.left + inflamed_value_bar_text_rect.width +10 ,\
                                           inflamed_value_bar_text_rect.top  , 100 , inflamed_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字
        player.check_value()
        inflamed_value_bar_num_text = font_15.render(str(player.inflamed_value), True , status_bar_font_color)
        inflamed_value_bar_num_text_rect = inflamed_value_bar_num_text.get_rect()
        inflamed_value_bar_num_text_rect.topleft =  r_i.right + 2 , inflamed_value_bar_text_rect.top 
        screen.blit(inflamed_value_bar_num_text , inflamed_value_bar_num_text_rect)

        
        # 绘制心情条
        # 绘制”心情“
        mood_value_bar_text = font_15.render('心情' , True , status_bar_font_color)
        mood_value_bar_text_rect = mood_value_bar_text.get_rect()
        mood_value_bar_text_rect.center = (screen_size_width / 18 * 5 +5 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(mood_value_bar_text ,  mood_value_bar_text_rect)
        # 绘制血条
        if 0 <= player.mood_value < 20 :
            pygame.draw.rect(screen , RED , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , player.mood_value , mood_value_bar_text_rect.height   ) )
        elif 20 <= player.mood_value <= 100 :
            pygame.draw.rect(screen , GREEN , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , player.mood_value , mood_value_bar_text_rect.height   ) )
        r_m = pygame.draw.rect(screen , status_bar_font_color , (mood_value_bar_text_rect.left + mood_value_bar_text_rect.width +10 ,\
                                           mood_value_bar_text_rect.top  , 100 , mood_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字
        player.check_value()
        mood_value_bar_num_text = font_15.render(str(player.mood_value), True , status_bar_font_color)
        mood_value_bar_num_text_rect = mood_value_bar_num_text.get_rect()
        mood_value_bar_num_text_rect.topleft =  r_m.right + 2 , mood_value_bar_text_rect.top 
        screen.blit(mood_value_bar_num_text , mood_value_bar_num_text_rect)

        # 绘制营养条
        # 绘制”营养“
        nutritional_value_bar_text = font_15.render('营养' , True , status_bar_font_color)
        nutritional_value_bar_text_rect = nutritional_value_bar_text.get_rect()
        nutritional_value_bar_text_rect.center = (screen_size_width / 18 * 9 +10 , screen_active_size[1] + (screen_size_height - screen_active_size[1]) // 2 )
        screen.blit(nutritional_value_bar_text ,  nutritional_value_bar_text_rect)
        # 绘制血条
        if (0 <= player.nutritional_value < 15) or (85 < player.nutritional_value <= 100)  :
            pygame.draw.rect(screen , RED , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , player.nutritional_value , nutritional_value_bar_text_rect.height   ) )
        elif 15 <= player.nutritional_value<= 85 :
            pygame.draw.rect(screen , GREEN , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , player.nutritional_value , nutritional_value_bar_text_rect.height   ) )
        r_n = pygame.draw.rect(screen , status_bar_font_color , (nutritional_value_bar_text_rect.left + nutritional_value_bar_text_rect.width +10 ,\
                                           nutritional_value_bar_text_rect.top  , 100 , nutritional_value_bar_text_rect.height   ) , 1)
        # 绘制血条数字
        player.check_value()
        nutritional_value_bar_num_text = font_15.render(str(player.nutritional_value), True , status_bar_font_color)
        nutritional_value_bar_num_text_rect = nutritional_value_bar_num_text.get_rect()
        nutritional_value_bar_num_text_rect.topleft =  r_n.right + 2 , nutritional_value_bar_text_rect.top 
        screen.blit(nutritional_value_bar_num_text , nutritional_value_bar_num_text_rect)
        
        # 绘制分数条
        score_text = font_15.render('分数：'+str(player.score) , True , status_bar_font_color)
        screen.blit(score_text , (screen_size_width / 18 * 13 + 10, nutritional_value_bar_text_rect.top ))

        # 绘制目标分数，倒计时
        target_text = font_20.render('目标分数：%d  倒计时：%d' % (target_score , target_time) , True , status_bar_font_color)
        target_text_rect = target_text.get_rect()
        target_text_rect.topleft= screen_size_width - target_text_rect.width -10 , 10
        screen.blit(target_text , target_text_rect)

        # 绘制开始暂停按钮,空格文字图片
        unpause_and_pause_button_image_rect.centery = screen_size_height - \
                                                      (screen_size_height - screen_active_size[1]) // 2
        unpause_and_pause_button_image_rect.right = screen_size_width - 10
        space_text_image_rect.right = unpause_and_pause_button_image_rect.left
        space_text_image_rect.top = unpause_and_pause_button_image_rect.top
        screen.blit(space_text_image , space_text_image_rect)
        if pause_status :
            screen.blit(pause_button_image , unpause_and_pause_button_image_rect)
        else :
            screen.blit(unpause_button_image , unpause_and_pause_button_image_rect)
            
        # 判断分数是否达到下一水果等级
        if player.score >= 25 and food_level == 1:
            food_level = 2
            # 创建初始v2食物，每种3个
            for food_name ,  food_inflamed_value , food_mood_value , food_nutritional_value , food_score \
                          in food_v2 :
                for i in range(3):
                    food = Food_v2(screen_active_size ,  \
                                       food_name , food_inflamed_value , \
                                       food_mood_value , food_nutritional_value , food_score )
                    food_group.add(food)
                    

        # 检测三个值是否满足游戏失败值     
        if player.inflamed_value_status or player.mood_value_status or player.nutritional_value_status:
            game_over = True
            start_game = False
            break
        
        # 更新屏幕
        pygame.display.update()
        clock.tick(60)

    delay = 0
    # 游戏结束界面
    while game_over :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == UPDATE_LOSER_TIME :
                loser.update()

        # 绘制失败文字图片
        screen.blit(defeat_image , defeat_image_rect)
        
        if delay >= 10:
            # 绘制失败者loser
            screen.blit(loser.image , loser.rect)
            
        if delay >=20:
            # 绘制失败原因
            defeat_beacuse_text.check(game_over_because_score , player.inflamed_value_status , player.mood_value_status , player.nutritional_value_status )
            screen.blit(defeat_beacuse_text.image , defeat_beacuse_text.rect)
            delay = 20
            
        if delay< 20:
            delay +=1
        # 更新屏幕
        pygame.display.update()
        clock.tick(10)
