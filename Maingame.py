import pygame
import timeconst
from typing import NamedTuple
import time


image_path = "/data/data/org.test.pythongame/files/app"
clock = pygame.time.Clock()
pygame.init() #initialize module, инициализирую модуль
screen = pygame.display.set_mode((1420,720),pygame.RESIZABLE)
screen_centerx = screen.get_width() // 2
screen_centerx = screen_centerx - 70
screen_centery = screen.get_height() // 2
screen_centery = screen_centery - 30

pygame.display.set_caption("First \"game\"")

kill_count = 0

running = True

font1 = pygame.font.Font("fonts\Oswald-VariableFont_wght.ttf",36)
kill_font = pygame.font.Font("fonts\Oswald-VariableFont_wght.ttf",50)

lose_text = font1.render("Game over!",True,(255, 255, 255))
kill_count_text = kill_font.render(str(kill_count),True,(255,255,255),)

restart_text = font1.render("Restart",True,(191, 242, 239))
#topleft=(screen_centerx + 23,screen_centery + 50)
restart_text_rect = restart_text.get_bounding_rect().move(screen_centerx + 23,screen_centery + 50)

background = pygame.image.load('images/drybambooforest.jpg').convert_alpha()

background = pygame.transform.scale(background,(1420,720))

background2 = pygame.image.load('images/greenbambooforest.jpg').convert_alpha()

background2 = pygame.transform.scale(background2,(1420,720))

octo = pygame.image.load('images/monster.png').convert_alpha()

octo = pygame.transform.scale(octo,(35,35))
#lists for images to make the animation 
walk_left = [
    pygame.image.load("images/Player/player_left1.png").convert_alpha(),
    pygame.image.load("images/Player/player_left2.png").convert_alpha(),
    pygame.image.load("images/Player/player_left3.png").convert_alpha(),
    pygame.image.load("images/Player/player_left4.png").convert_alpha(),
]

walk_right = [
    pygame.image.load("images/Player/player_right1.png").convert_alpha(),
    pygame.image.load("images/Player/player_right2.png").convert_alpha(),
    pygame.image.load("images/Player/player_right3.png").convert_alpha(),
    pygame.image.load("images/Player/player_right4.png").convert_alpha(),
]
#coordinates
octo_x = 1420
octo_y = 550
octo_list_in_game = []
player_speed = 5
el_speed = 10
player_x = 200
player_y = 550
player_anim_count = 0
background_x = 0
is_jump = False
jump_count = 7
octo_timer = pygame.USEREVENT + 1
pygame.time.set_timer(octo_timer,2500)
start_time = timeconst.now_time
print(start_time)
bullet = pygame.image.load("images/bullet.png").convert_alpha()
bullet = pygame.transform.scale(bullet,(20,20))
bullet_rotate = pygame.transform.rotate(bullet,90)
bullet_rotate = pygame.transform.scale(bullet_rotate,(50,70)).convert_alpha()
bullet_rect = bullet.get_bounding_rect().move(player_x + 140,player_y + 115)
bullets = []
bullet_count = 3


#animation of the player, анимация движения
if player_anim_count == 3:
    player_anim_count = 0
else:
    player_anim_count += 1
#octo_rect = octo.get_rect(topleft=(octo_x,octo_y))

gameplay = True
#—— тут,с помощью усл.конструкции единожды заполняю экран цветом
flag = False # +++
flag2 = True

#бескон. цикл,необходимый для беспрерывной работы программы 
while running:
    end_time = time.time()
    clock.tick(16)
    #——
    if not flag:  # +++
        screen.fill((22, 12, 89))
        flag = True
        #——
    #setting the background images
    keys = pygame.key.get_pressed()
    screen.blit(background,(background_x,0))
    screen.blit(background2,(background_x + 1420,0))
    flag2 = True
    if gameplay:
        end_time = time.strftime("%H:%M:%S")
        end_time = end_time.split(":")
        while True:
            print(end_time)
            if 1 == 1:
                break
        
        # end_time - start_time
        # if end_time - start_time >= 5 and bullet_count <= 3 and flag2:
        #     if flag2:
        #         bullet_count += 1
        #         flag2 = False
        #     end_time = time.time()

        #Ammo and kills
        screen.blit(kill_count_text,(1340,10))
        if bullet_count == 4:
            screen.blit(bullet_rotate,(40,20))
            screen.blit(bullet_rotate,(80,20))
            screen.blit(bullet_rotate,(120,20))
            screen.blit(bullet_rotate,(160,20))
        elif bullet_count == 3:
            screen.blit(bullet_rotate,(40,20))
            screen.blit(bullet_rotate,(80,20))
            screen.blit(bullet_rotate,(120,20))
        elif bullet_count == 2:
            screen.blit(bullet_rotate,(40,20))
            screen.blit(bullet_rotate,(80,20))
        elif bullet_count == 1:
            screen.blit(bullet_rotate,(40,20))
        #ставлю квадрат в центр игрока,потому что иначе касания с врагами регистрируються слишком рано
        #get_rect(center=(player_x,player_y),topleft=(player_x,player_y))
        #midleft=(player_x,player_y),midright=(player_x,player_y),width=10
        player_rect = walk_left[player_anim_count].get_bounding_rect().move(player_x,player_y)

        if octo_list_in_game:
            for (i,el) in enumerate(octo_list_in_game):
                screen.blit(octo,el)
                el.x -= el_speed
                if el.x < -60:
                    octo_list_in_game.pop(i)
                    #and player_rect.x >= el.x
                if player_rect.colliderect(el):
                    gameplay = False
                    print("octo midright: ",el.midright)
                    print("octo midleft: ",el.midleft)
                    print("octo midtop: ",el.midtop)
                    print("octo midbottom: ",el.midbottom)
                    print("octo center: ",el.center)
                    print("player midright: ",player_rect.midright)
                    print("player midleft: ",player_rect.midleft)
                    print("player midtop: ",player_rect.midtop)
                    print("player midbottom: ",player_rect.midbottom)
                    print("player center: ",player_rect.center)
                    print("player width",player_rect.width)
                    

        # octo_rect = octo.get_rect(topleft=(octo_x,octo_y))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            screen.blit(walk_right[player_anim_count], (player_x,player_y))
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x,player_y))

        # keys = pygame.key.get_pressed()
        #player movement, Передвижение игрока
        
        if not not keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 1000 or not not keys[pygame.K_RIGHT] or keys[pygame.K_d] and keys[pygame.K_LCTRL]:
            player_x += player_speed
            if not not keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_y += player_speed
            if not not keys[pygame.K_UP] or keys[pygame.K_w]:
                player_y -= player_speed

        elif not not keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 25 or not not keys[pygame.K_LEFT] or keys[pygame.K_a] and keys[pygame.K_LCTRL]:
            player_x -= player_speed
            if not not keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_y += player_speed
            if not not keys[pygame.K_UP] or keys[pygame.K_w]:
                player_y -= player_speed
        elif not not keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= player_speed

        elif not not keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += player_speed

        elif not not keys[pygame.K_LSHIFT]:
            player_speed = 50
        elif not keys[pygame.K_LSHIFT]:
            player_speed = 5    
        #jump logic,логика прыжка
        if not is_jump:
            if not not keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                    clock.tick(100)
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
                clock.tick(100)
            else:
                is_jump = False
                jump_count = 7

        
        #background movement, Передвижение заднего изображения
        background_x -= 5
        if background_x == -1420:
            background_x = 0

#animation of the player, анимация движения
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1
        
        
        # if not not keys[pygame.K_f] and len(bullets) <= 2:
            #topleft=(player_x + 20,player_y)
     #bullet and octo collision       
        if bullets:
            for (i,el) in enumerate(bullets):
                screen.blit(bullet,(el.x,el.y))
                el.x += 15
                if el.x > 1440:
                    bullets.pop(i)
                if octo_list_in_game:
                    for (index,octopus) in enumerate(octo_list_in_game):
                        if el.colliderect(octopus):
                            octo_list_in_game.pop(index)
                            bullets.pop(i)
                            bullet_count += 1
                            kill_count += 1
    #game over screen,lose screen
    else:
        screen.fill((35, 5, 125))
        screen.blit(lose_text,(screen_centerx,screen_centery))
        screen.blit(restart_text,restart_text_rect)
        mouse = pygame.mouse.get_pos()
        # if pygame.mouse.get_pressed() and restart_text_rect.collidepoint(mouse):
        #     gameplay = True
        #     player_x = 200
        #     player_y = 550
        #     octo_list_in_game.clear()
        #     background_x = 0
        
    icon_ganesha = pygame.image.load("images/ganesha.png").convert_alpha()
    pygame.display.set_icon(icon_ganesha)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_INSERT:
                screen.fill((109, 94, 204))
                pygame.display.update()
            elif event.key == pygame.K_DELETE:
                screen.fill((22, 12, 89))
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and restart_text_rect.collidepoint(mouse):
            if event.button == 1:
                gameplay = True
            player_x = 200
            player_y = 550
            octo_list_in_game.clear()
            background_x = 0
            bullets.clear()
        if gameplay and  event.type == pygame.KEYUP and event.key == pygame.K_f and len(bullets) <= 3 and bullet_count > 0:
            bullets.append(bullet.get_bounding_rect().move(player_x + 140,player_y + 115))
            bullet_count -= 1


        if event.type == octo_timer:
            #pygame.draw.circle(octo,"Blue",(1420,650),5,1
            #midleft=(1370,680),midright=(1420,680),midtop=(1395,655),midbottom=(1395,705),width=10
            octo_list_in_game.append(octo.get_bounding_rect().move(1420,675))
    # clock.tick(12)