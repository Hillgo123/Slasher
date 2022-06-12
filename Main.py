import pygame, sys, random, time
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()

from Definitions import *

from Assets import *
 
#To do
#https://trello.com/b/kxFIVWqz/player

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, health, max_health, health_bar, target_health):
        super().__init__()
        #self.image.set_colorkey(WHITE)
       
        self.animating_D = False
        self.animating_UP = False
        self.animating_LEFT = False
        self.animating_RIGHT = False

        self.sprites_down = []
        self.sprites_down.append(walk_D1)
        self.sprites_down.append(walk_D2)
        self.sprites_down.append(walk_D3)
        self.sprites_down.append(walk_D4)
        self.current_sprite_down = 0

        self.sprites_up = []
        self.sprites_up.append(walk_UP1)
        self.sprites_up.append(walk_UP2)
        self.sprites_up.append(walk_UP3)
        self.sprites_up.append(walk_UP4)
        self.current_sprite_up = 0

        self.sprites_Left = []
        self.sprites_Left.append(walk_L1)
        self.sprites_Left.append(walk_L2)
        self.sprites_Left.append(walk_L3)
        self.sprites_Left.append(walk_L4)
        self.current_sprite_left = 0

        self.sprites_Right = []
        self.sprites_Right.append(walk_R1)
        self.sprites_Right.append(walk_R2)
        self.sprites_Right.append(walk_R3)
        self.sprites_Right.append(walk_R4)
        self.current_sprite_right = 0

        self.image = self.sprites_down[self.current_sprite_down]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.hitbox = self.image.get_rect()
        self.health = health
        self.max_health = max_health
        self.health_bar = health_bar
        self.target_health = target_health
        self.health_ratio = self.max_health / self.health_bar


    #Movement

    def animation(self):

        #Animations

        if self.animating_D == True:
            self.current_sprite_down += 0.05

            if self.current_sprite_down >= len(self.sprites_down):
                self.current_sprite_down = 0 
                self.animating_D = False

            self.image = self.sprites_down[int(self.current_sprite_down)]

        if self.animating_UP == True:
            self.current_sprite_up += 0.05

            if self.current_sprite_up >= len(self.sprites_up):
                self.current_sprite_up = 0 
                self.animating_UP = False

            self.image = self.sprites_up[int(self.current_sprite_up)]


        if self.animating_LEFT == True:
            self.current_sprite_left += 0.05

            if self.current_sprite_left >= len(self.sprites_up):
                self.current_sprite_left = 0 
                self.animating_LEFT = False

            self.image = self.sprites_Left[int(self.current_sprite_left)]

        if self.animating_RIGHT == True:
            self.current_sprite_right += 0.05

            if self.current_sprite_right >= len(self.sprites_Right):
                self.current_sprite_right = 0 
                self.animating_RIGHT = False

            self.image = self.sprites_Right[int(self.current_sprite_right)]

    def move(self):
        #Movement
        pos_x = 0
        pos_y = 0

        #Keypresses
        key = pygame.key.get_pressed()
       
        if key[K_w]:
            pos_y -= 1 * self.speed
            #self.hitbox -= 1 * self.speed
            self.animating_UP = True
        if key[K_s]:
            pos_y += 1 * self.speed
            #self.hitbox += 1 * self.speed
            self.animating_D = True
        if key[K_a]:
            pos_x += 1 * self.speed
            #self.hitbox += 1 * self.speed
            self.animating_LEFT = True
        if key[K_d]:
            pos_x -= 1 * self.speed
            #self.hitbox -= 1 * self.speed
            self.animating_RIGHT = True
           

        #Screen borders
        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.y > (screen_height - 40):
            self.rect.y = screen_height - 40

        if self.rect.x < 25:
            self.rect.x = 25

        if self.rect.x > screen_width - 50:
            self.rect.x = screen_width - 50
        #Dash
        global dash_counter_cooldown
        dash_counter_cooldown += clock.get_time()
        if dash_counter_cooldown > dash_cooldown:
            dash_counter_cooldown= 0



        if key[K_w] and key[K_SPACE] and dash_counter_cooldown == 0: 
            pos_y -= 50 * self.speed
        if key[K_s] and key[K_SPACE] and dash_counter_cooldown == 0: 
            pos_y += 50 * self.speed
        if key[K_a] and key[K_SPACE] and dash_counter_cooldown == 0: 
            pos_x += 50 * self.speed
        if key[K_d] and key[K_SPACE] and dash_counter_cooldown == 0: 
           pos_x -= 50 * self.speed

        

        self.rect.x -= pos_x
        self.rect.y += pos_y

        
        #if key[pygame.K_f]:
        #    print(clock.get_fps())
        #self.hitbox = self.rect.center



        screen.blit(self.image, self.rect)

    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            dead = True

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health
    
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0),(50,10,self.target_health / self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(50,10,self.health_bar,25),4)
        key = pygame.key.get_pressed()
        if key[K_UP]:
            self.get_health(20)
        
        if Enemy.hitbox.colliderect(self.hitbox):
            self.get_damage(enemy_atc)
            
        #if self.health == 0:
         #   dead = True
    
            
    #def collision(self):
    #    #if Enemy.hitbox.colliderect(self):
    #    if pygame.Rect.colliderect(Enemy.hitbox):
    #     
    #        print("yes")

    def update(self):
        self.animation()
        self.move()
        self.basic_health()
        #self.collision()

#pygame.sprite.Sprite
class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.animating_D = False
        self.animating_UP = False
        self.animating_LEFT = False
        self.animating_RIGHT = False

        self.sprites_down = []
        self.sprites_down.append(E_walk_D1)
        self.sprites_down.append(E_walk_D2)
        self.sprites_down.append(E_walk_D3)
        self.sprites_down.append(E_walk_D4)
        self.current_sprite_down = 0

        self.sprites_up = []
        self.sprites_up.append(E_walk_UP1)
        self.sprites_up.append(E_walk_UP2)
        self.sprites_up.append(E_walk_UP3)
        self.sprites_up.append(E_walk_UP4)
        self.current_sprite_up = 0

        self.sprites_Left = []
        self.sprites_Left.append(E_walk_L1)
        self.sprites_Left.append(E_walk_L2)
        self.sprites_Left.append(E_walk_L3)
        self.sprites_Left.append(E_walk_L4)
        self.current_sprite_left = 0

        self.sprites_Right = []
        self.sprites_Right.append(E_walk_R1)
        self.sprites_Right.append(E_walk_R2)
        self.sprites_Right.append(E_walk_R3)
        self.sprites_Right.append(E_walk_R4)
        self.current_sprite_right = 0

        self.image = self.sprites_down[self.current_sprite_down]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.center = [x, y]
        self.hitbox = self.image.get_rect()


    def move(self):
        dirvect = pygame.math.Vector2(Player.rect.x - self.rect.x, Player.rect.y - self.rect.y)
        if dirvect.length_squared() > 0:
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
        


        if self.rect.y < Player.rect.y:
            self.animating_D = True



        screen.blit(self.image, self.rect)

    def animations(self):
        if self.animating_D == True:
            self.current_sprite_down += 0.05

            if self.current_sprite_down >= len(self.sprites_down):
                self.current_sprite_down = 0 
                self.animating_D = False
            self.image = self.sprites_down[int(self.current_sprite_down)]
        
            
        

    def create_enemy(self):        
        global enemies
        if len(enemies) < max_zombie_count:
            
            new_enemy = enemy(random.randint(1, 1980), random.randint(1, 1080), Enemy_zombie_speed)               
            enemies.append(new_enemy)

        
    

    def collision(self):
        if Player.hitbox.colliderect(self.hitbox):
            print("yes")
       
    def kill(self):
        
        if key[K_LSHIFT]:
            self.kill()
            

    def update(self):
        self.create_enemy()
        for Enemy in enemies:
            Enemy.move()
        self.collision()
        #self.kill()

class game_state():
    def __init__(self):
        self.state = 'start'

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()

        if key[K_SPACE]:
            self.state = 'main_game'
            dead = False

        screen.fill((100, 100, 100))

        
                
        screen.blit(start, (screen_width/2 - 100, screen_height/2 - 12.5))
         

        pygame.display.flip()

    def main_game(self):
        
        screen.fill((100, 100, 100))
        
        
        player_sprite.update()
        enemy_sprite.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()

        if key[K_q]:
            self.state = 'game_over'
        if dead == True:
            self.state = 'game_over'
        pygame.display.flip()

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()

        if key[K_SPACE]:
            self.state = 'main_game'

        screen.fill((100, 100, 100))

        
                
        screen.blit(game_over, (screen_width/2 - 100, screen_height/2 - 50))
         

        pygame.display.flip()

    def state_manager(self):
        if self.state == 'start':
            self.start()

        if self.state == 'main_game':
            self.main_game()

        if self.state == 'game_over':
            self.game_over()
          

        
player_sprite = pygame.sprite.Group()
enemy_sprite = pygame.sprite.Group()


Player = player(start_x, start_y, player_speed, player_health, player_max_health, player_health_bar, player_target_health)

Enemy = enemy(enemy_start_x, enemy_start_x, Enemy_zombie_speed)
enemies = []

player_sprite.add(Player)
enemy_sprite.add(Enemy)

Game_State = game_state()


def main():
    run = True
    while run:
        clock.tick(FPS)

        Game_State.state_manager()


    pygame.quit()

if __name__ == "__main__":
    main()

