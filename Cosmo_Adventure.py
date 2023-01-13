import pygame.mixer_music
from iteration_utilities import duplicates
from game_data.classes import attack
from game_data.classes import enemy
from game_data.options import *
import random
run = True
count = 2
Enemy_MaxSpeed = 30
Max_Bullets = 8
enemy_ = []
Level_Max_enemy = 2
Level = 1
win = pygame.display.set_mode((root_x, root_y))
pygame.display.set_caption("Cosmo Adventure")
clock = pygame.time.Clock()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
def check():
    if len(duplicates_enemy) > 0:
        for d in duplicates_enemy:
            enemy_speed = random.randint(15, Enemy_MaxSpeed)
            enemy_color = (255, 1*(enemy_speed * 8), 255)
            enemy_options.append([random.randint(50, virtual_pres_cord_x + 10),
                                  random.randint(1, virtual_pres_cord_y - 2), enemy_speed, enemy_color])
            enemy_options.remove(d)
def sort(enemy_options):
    for run in range((len(enemy_options)-1)):
        for i in range(len(enemy_options)-1-run):
            if enemy_options[i][3][1]>enemy_options[i+1][3][1]:
                enemy_options[i],enemy_options[i+1] = enemy_options[i+1], enemy_options[i]
def generate(count):
    global duplicates_enemy, enemy_x, enemy_y
    for i in range(count):
        enemy_speed = random.randint(15, Enemy_MaxSpeed)
        enemy_color = (255, 1*(enemy_speed * 8), 255)
        enemy_x = random.randint(50, virtual_pres_cord_x + 10)
        enemy_y = random.randint(1, virtual_pres_cord_y - 2)
        enemy_options.append([enemy_x, enemy_y, enemy_speed, enemy_color])
    while True:
        duplicates_enemy = list(duplicates(enemy_options))
        check()
        if len(duplicates_enemy) == 0:
            break
    sort(enemy_options)
def enemy_creator():
    global enemy_
    for s in range(len(enemy_options)):
        enemy_.append(enemy((enemy_options[s][0]*40), (enemy_options[s][1]*enemy_size), (enemy_options[s][2]),
                            enemy_size, enemy_size, enemy_options[s][3]))
generate(count)
enemy_creator()
def painter():
    global niga
    pygame.display.update()
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    for enemy in enemy_:
        enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    if anim == True:
        win.blit(going, (x, y))
    else:
        win.blit(stoped, (x, y))
    text1 = f1.render("Level - {}".format(Level), 1, (180, 0, 0))
    text2 = f1.render("max bullets - {}".format(int(Max_Bullets)+1), 1, (180, 0, 0))
    win.blit(text2, (root_x - 200, 10))
    win.blit(text1, (10, 10))
bullet_sound.set_volume(0.2)
enemy_sound.set_volume(0.4)
pygame.mixer.music.play(-1)
pygame.display.set_icon(icon)
while run:
    pygame.init()
    pygame.mouse.set_visible(False)
    for enes in range(len(enemy_)+1):
        if len(enemy_) == 0:
            run = True
            Level += 1
            Enemy_MaxSpeed = 30
            Max_Bullets *= 1.1
            enemy_ = []
            speed = 3
            if Level_Max_enemy == 2 or Level_Max_enemy == 3:
                Level_Max_enemy *= 1.5
            else:
                Level_Max_enemy *= 1.25
            count = Level_Max_enemy
            dash = 10
            enemy_size = 40
            x = 1920 / 2 - 500
            y = 1080 / 2
            virtual_pres_cord_x = root_x / enemy_size
            virtual_pres_cord_y = root_y / enemy_size
            bullets = []
            anim = False
            enemy_options = []
            print(count)
            generate(int(count))
            print(enemy_options)
            enemy_creator()
    painter()
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if len(bullets) <= Max_Bullets:
                    if len(bullets) <= Max_Bullets:
                        bullets.append(attack(((x + width // 2)*1+70), (y + height // 2), 10, (255, 50, 0)))
                        bullet_sound.play()
                    if len(bullets) <= Max_Bullets:
                        bullets.append(attack(((x + width // 2) * 1 + 70), (y + height // 2 - 63), 10, (255, 50, 0)))
                        bullet_sound.play()
                    if len(bullets) <= Max_Bullets:
                        bullets.append(attack(((x + width // 2) * 1 + 70), (y + height // 2 + 63), 10, (255, 50, 0)))
                        bullet_sound.play()
    for bullet in bullets:
        if bullet.x < root_x and bullet.x > 0:
            bullet.x += bullet.vel*wal
        else:
            bullets.pop(bullets.index(bullet))
    for enems in enemy_:
        if enems.x < root_x + 500 and enems.x > 0:
            enems.x -= 1 * ((enems.speed) * 0.1)
        else:
            run = True
            Level = 1
            Enemy_MaxSpeed = 30
            Max_Bullets = 8
            enemy_ = []
            speed = 3
            Level_Max_enemy = 2
            count = Level_Max_enemy
            dash = 10
            enemy_size = 40
            x = 1920 / 2 - 500
            y = 1080 / 2
            virtual_pres_cord_x = root_x / enemy_size
            virtual_pres_cord_y = root_y / enemy_size
            bullets = []
            anim = False
            enemy_options = []
            pygame.mixer.music.rewind()
            print(count)
            generate(int(count))
            print(enemy_options)
            enemy_creator()
    for enems in enemy_:
        if enems.x >= x and enems.x <= x + width  and enems.y >= y and enems.y <= y + height:
            run = True
            Level = 1
            Enemy_MaxSpeed = 30
            Max_Bullets = 8
            enemy_ = []
            speed = 3
            Level_Max_enemy = 2
            count = Level_Max_enemy
            dash = 10
            enemy_size = 40
            x = 1920 / 2 - 500
            y = 1080 / 2
            virtual_pres_cord_x = root_x / enemy_size
            virtual_pres_cord_y = root_y / enemy_size
            bullets = []
            anim = False
            enemy_options = []
            pygame.mixer.music.rewind()
            print(count)
            generate(int(count))
            print(enemy_options)
            enemy_creator()
    for enem in enemy_:
        for bullet in bullets:
            if bullet.x-10 >= enem.x-10 and bullet.x+10 <= enem.x + 10 + enemy_size and bullet.y-5 >= enem.y - 5 and bullet.y+5 \
                    <= enem.y+5 + enemy_size:
                bullets.pop(bullets.index(bullet))
                enemy_.pop(enemy_.index(enem))
                enemy_sound.play()
    if keys[pygame.K_w] and keys[pygame.K_a] and y > 0 and x > 0:
        y -= speed-2
        x -= speed-2
        anim = True
    if keys[pygame.K_w] and keys[pygame.K_d] and y > 0 and x < root_x - width:
        y -= speed
        x += speed
        anim = True
    if keys[pygame.K_a] and keys[pygame.K_s] and y < root_y - height and x > 0:
        x -= speed
        y += speed
        anim = True
    if keys[pygame.K_a] and keys[pygame.K_w] and y > 0 and x > 0:
        x -= speed
        y -= speed
        anim = True
    if keys[pygame.K_s] and keys[pygame.K_d] and y < root_y - height and x < root_x - width:
        x += speed
        y += speed
        anim = True
    if keys[pygame.K_w] and y > 0:
        y -= speed
        anim = True
        if keys[pygame.K_SPACE]:
            y -= dash
    elif keys[pygame.K_s] and y < root_y - height:
        y += speed
        anim = True
        if keys[pygame.K_SPACE]:
            y += dash
    elif keys[pygame.K_a] and x > 0:
        x -= speed
        anim = False
        if keys[pygame.K_SPACE]:
            x -= dash
    elif keys[pygame.K_d] and x < root_x - width:
        x += speed
        anim = True
        if keys[pygame.K_SPACE]:
            x += dash
    else:
        anim = False
    clock.tick(75)
pygame.quit()
