import sys , pygame
from pygame.locals import *
from materials import *

game_menu = True
start_game = False

clock = pygame.time.Clock()

while True:
    delay = 100
    while game_menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 判断按钮是否被按下
            if event.type == MOUSEBUTTONDOWN:
                temp = start_game_button.is_or_not_press()
                if temp :
                    start_game = True
                    game_menu = False
                    break
                
        # 绘制背景
        screen.blit(game_menu_background_image , game_menu_background_image_rect)
        screen.fill((255 , 255 , 255))
        
        # 绘制界面文字按钮
        start_game_button.is_or_not_in_and_blit(screen)

        pygame.display.update()
        clock.tick(10)

    # 开始游戏
    while start_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 绘制背景
        screen.blit(start_game_background_image , start_game_background_image_rect)
        screen.fill((255 , 255 , 255))

        # 绘制玩家
        player.check()
        screen.blit(player.image , player.rect)

        # 绘制食物
        for each in food_group:
            each.move()
            screen.blit(each.image , each.rect)

        # 绘制上火条
        pygame.draw.rect()
        
        pygame.display.update()
        clock.tick(60)
