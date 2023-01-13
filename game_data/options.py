import pygame
root_x = 1920
root_y = 1080
width = 250
height = 150
speed = 3
dash = 10
enemy_size = 40
x = 1920/2 - 500
y = 1080/2
virtual_pres_cord_x = root_x/enemy_size
virtual_pres_cord_y = root_y/enemy_size
f1 = pygame.font.Font(None, 36)
bullets = []
enemy_options = []
color = (250, 0, 0)
wal = 1
anim = False
stoped = pygame.image.load("game_data/resources/player.png")
going = pygame.image.load("game_data/resources/player_2.png")
background = pygame.image.load("game_data/resources/background.gif")
icon = pygame.image.load("game_data/resources/icon.png")
pygame.mixer_music.load('game_data/resources/music.mp3')
bullet_sound = pygame.mixer.Sound('game_data/resources/bullet_sound.ogg')
enemy_sound = pygame.mixer.Sound('game_data/resources/vspyishka-lazera.ogg')
