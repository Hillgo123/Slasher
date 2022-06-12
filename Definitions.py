import pygame, random
from pygame.locals import *

pygame.init()


FPS = 120
clock = pygame.time.Clock()

key = pygame.key.get_pressed()

#Screen
screen_width = 1980
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

BLACK = 255, 255, 255
WHITE = 0, 0, 0

#Player definitions
player_speed = 2
start_x = 100
start_y = 100
player_health = 100
player_max_health = 100
player_health_bar = 500
player_target_health = 100

dead = False


dash_counter_cooldown = 0
dash_cooldown = 200
dash_counter_duration = 100
dash_duration = 100

#Enemy definitions
Enemy_zombie_speed = 3
max_zombie_count = 3

enemy_start_x = random.randint(1, 1980)
enemy_start_y = random.randint(1, 1980)

enemy_atc = 0.5
