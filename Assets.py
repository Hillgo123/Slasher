
#This file is used to load Assets

import pygame
from pygame.locals import *

pygame.init()

#Images

bg = pygame.image.load("Images/bg.png")


#Player assets credit pixel-boi https://pixel-boy.itch.io/ninja-adventure-asset-pack
walk_D1 = pygame.image.load("Images/Walk_D1.png")
walk_D1 = pygame.transform.scale(walk_D1, (30, 60))
walk_D2 = pygame.image.load("Images/Walk_D2.png")
walk_D2 = pygame.transform.scale(walk_D2, (30, 60))
walk_D3 = pygame.image.load("Images/Walk_D3.png")
walk_D3 = pygame.transform.scale(walk_D3, (30, 60))
walk_D4 = pygame.image.load("Images/Walk_D4.png")
walk_D4 = pygame.transform.scale(walk_D4, (30, 60))

walk_UP1 = pygame.image.load("Images/Walk_UP1.png")
walk_UP1 = pygame.transform.scale(walk_UP1, (30, 60))
walk_UP2 = pygame.image.load("Images/Walk_UP2.png")
walk_UP2 = pygame.transform.scale(walk_UP2, (30, 60))
walk_UP3 = pygame.image.load("Images/Walk_UP3.png")
walk_UP3 = pygame.transform.scale(walk_UP3, (30, 60))
walk_UP4 = pygame.image.load("Images/Walk_UP4.png")
walk_UP4 = pygame.transform.scale(walk_UP4, (30, 60))

walk_L1 = pygame.image.load("Images/Walk_L1.png")
walk_L1 = pygame.transform.scale(walk_L1, (30, 60))
walk_L2 = pygame.image.load("Images/Walk_L2.png")
walk_L2 = pygame.transform.scale(walk_L2, (30, 60))
walk_L3 = pygame.image.load("Images/Walk_L3.png")
walk_L3 = pygame.transform.scale(walk_L3, (30, 60))
walk_L4 = pygame.image.load("Images/Walk_L4.png")
walk_L4 = pygame.transform.scale(walk_L4, (30, 60))

walk_R1 = pygame.image.load("Images/Walk_R1.png")
walk_R1 = pygame.transform.scale(walk_R1, (30, 60))
walk_R2 = pygame.image.load("Images/Walk_R2.png")
walk_R2 = pygame.transform.scale(walk_R2, (30, 60))
walk_R3 = pygame.image.load("Images/Walk_R3.png")
walk_R3 = pygame.transform.scale(walk_R3, (30, 60))
walk_R4 = pygame.image.load("Images/Walk_R4.png")
walk_R4 = pygame.transform.scale(walk_R4, (30, 60))

#Enemy assetscredit pixel-boi https://pixel-boy.itch.io/ninja-adventure-asset-pack
E_walk_D1 = pygame.image.load("Images/E_Walk_D1.png")
E_walk_D1 = pygame.transform.scale(E_walk_D1, (30, 60))
E_walk_D2 = pygame.image.load("Images/E_Walk_D2.png")
E_walk_D2 = pygame.transform.scale(E_walk_D2, (30, 60))
E_walk_D3 = pygame.image.load("Images/E_Walk_D3.png")
E_walk_D3 = pygame.transform.scale(E_walk_D3, (30, 60))
E_walk_D4 = pygame.image.load("Images/E_Walk_D4.png")
E_walk_D4 = pygame.transform.scale(E_walk_D4, (30, 60))

E_walk_UP1 = pygame.image.load("Images/E_Walk_UP1.png")
E_walk_UP1 = pygame.transform.scale(E_walk_UP1, (30, 60))
E_walk_UP2 = pygame.image.load("Images/E_Walk_UP2.png")
E_walk_UP2 = pygame.transform.scale(E_walk_UP2, (30, 60))
E_walk_UP3 = pygame.image.load("Images/E_Walk_UP3.png")
E_walk_UP3 = pygame.transform.scale(E_walk_UP3, (30, 60))
E_walk_UP4 = pygame.image.load("Images/E_Walk_UP4.png")
E_walk_UP4 = pygame.transform.scale(E_walk_UP4, (30, 60))

E_walk_L1 = pygame.image.load("Images/E_Walk_L1.png")
E_walk_L1 = pygame.transform.scale(E_walk_L1, (30, 60))
E_walk_L2 = pygame.image.load("Images/E_Walk_L2.png")
E_walk_L2 = pygame.transform.scale(E_walk_L2, (30, 60))
E_walk_L3 = pygame.image.load("Images/E_Walk_L3.png")
E_walk_L3 = pygame.transform.scale(E_walk_L3, (30, 60))
E_walk_L4 = pygame.image.load("Images/E_Walk_L4.png")
E_walk_L4 = pygame.transform.scale(E_walk_L4, (30, 60))

E_walk_R1 = pygame.image.load("Images/E_Walk_R1.png")
E_walk_R1 = pygame.transform.scale(E_walk_R1, (30, 60))
E_walk_R2 = pygame.image.load("Images/E_Walk_R2.png")
E_walk_R2 = pygame.transform.scale(E_walk_R2, (30, 60))
E_walk_R3 = pygame.image.load("Images/E_Walk_R3.png")
E_walk_R3 = pygame.transform.scale(E_walk_R3, (30, 60))
E_walk_R4 = pygame.image.load("Images/E_Walk_R4.png")
E_walk_R4 = pygame.transform.scale(E_walk_R4, (30, 60))

start = pygame.image.load("Images/Start.png")
game_over = pygame.image.load("Images/game_over.png")

lightsaber_img = pygame.image.load("Images/guy.png")

zombie_left_img = pygame.image.load("Images/Zombie.png")
zombie_right_img = pygame.transform.flip(zombie_left_img, 1, 0)

dirt = pygame.image.load("Images/Dirt.png")
grass = pygame.image.load("Images/grass.png")
#start_menu = pygame.image.load("Images/start.png")