# =============================================================================
# Import packages
# =============================================================================

import pygame
from sys import exit
from random import randint, choice


# =============================================================================
# Classes
# =============================================================================

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # walking animations
        
        walk_1 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (1).png"),0,0.3).convert_alpha()
        walk_2 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (2).png"),0,0.3).convert_alpha()
        walk_3 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (3).png"),0,0.3).convert_alpha()
        walk_4 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (4).png"),0,0.3).convert_alpha()
        walk_5 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (5).png"),0,0.3).convert_alpha()
        walk_6 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (6).png"),0,0.3).convert_alpha()
        walk_7 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (7).png"),0,0.3).convert_alpha()
        walk_8 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (8).png"),0,0.3).convert_alpha()
        walk_9 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (9).png"),0,0.3).convert_alpha()
        walk_10 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Walk (10).png"),0,0.3).convert_alpha()
        
        self.walking_frames_list = [walk_1, walk_2, walk_3, walk_4, walk_5, walk_6, walk_7, walk_8, walk_9, walk_10]
        self.walking_frame_index = 0
        
        # jumping animations
        
        jump_1 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Jump (5).png"),0,0.3).convert_alpha()
        jump_2 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Jump (6).png"),0,0.3).convert_alpha()
        jump_3 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Jump (7).png"),0,0.3).convert_alpha()
        jump_4 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Jump (8).png"),0,0.3).convert_alpha()
        jump_5 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Jump (9).png"),0,0.3).convert_alpha()
        
        
        self.jumping_frames_list = [jump_1, jump_2, jump_3, jump_4, jump_5]
        self.jumping_frame_index = 0
        
        # images 
        
        self.image = self.walking_frames_list[self.walking_frame_index]
        self.rect = self.image.get_rect(midbottom = (160,610))
        
        # variables
        
        self.gravity = 0
        
        # sound
        
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
        
    def player_input(self):
        # imput for jumping
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 620:
            self.gravity = -22
            self.jump_sound.play()
            
    def apply_gravity(self):
        # applying gravity
        self.gravity += 0.8
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 620:
            self.rect.bottom = 620

    def animate_dinosaur(self):
        if self.rect.y < 480:
            self.jumping_frame_index += 0.14
            if self.jumping_frame_index > len(self.jumping_frames_list):
                self.jumping_frame_index = 0
            self.image = self.jumping_frames_list[int(self.jumping_frame_index)]       
        else:
            self.walking_frame_index += 0.2
            self.jumping_frame_index = 0
            if self.walking_frame_index > len(self.walking_frames_list):
                self.walking_frame_index = 0
            self.image = self.walking_frames_list[int(self.walking_frame_index)]
            
        
    def update(self):
        self.animate_dinosaur()
        self.player_input()
        self.apply_gravity()
        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Enemy 1
        
        walk_1 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (1).png"),0,0.4).convert_alpha()
        walk_2 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (2).png"),0,0.4).convert_alpha()
        walk_3 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (3).png"),0,0.4).convert_alpha()
        walk_4 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (4).png"),0,0.4).convert_alpha()
        walk_5 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (5).png"),0,0.4).convert_alpha()
        walk_6 = pygame.transform.rotozoom(pygame.image.load("Graphics/enemies/Walk (6).png"),0,0.4).convert_alpha()
        
        self.walking_frames_list = [walk_1, walk_2, walk_3, walk_4, walk_5, walk_6]
        self.walking_frame_index = 0
        
        self.image = self.walking_frames_list[self.walking_frame_index]
        self.rect = self.image.get_rect(midbottom = (randint(1000,1200),620))
        
        
    def animate_enemy(self):     
        
        self.walking_frame_index += 0.15
        if self.walking_frame_index > len(self.walking_frames_list):
            self.walking_frame_index = 0
        self.image = self.walking_frames_list[int(self.walking_frame_index)] 
        
    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()
        
    def update(self):
        self.rect.x -= 5
        self.animate_enemy()
        self.destroy()
        
        
# =============================================================================
# Funcions
# =============================================================================

def animate_idle():
    global idle_surf, idle_frame_index
    idle_frame_index += 0.15
    if idle_frame_index > len(idle_surface_list):
            idle_frame_index = 0
    idle_surf = idle_surface_list[int(idle_frame_index)] 
    
def animate_dead():
    global dead_surf, dead_frame_index
    if int(dead_frame_index) < len(dead_surface_list)-1:
        dead_frame_index += 0.08
        dead_surf = dead_surface_list[int(dead_frame_index)]
    else:
         dead_surf = dead_surface_list[7] 
       

def collision_sprite():
    lives = game_lives
    if pygame.sprite.spritecollide(dinosaur.sprite,enemy_group,False):
        # delete all the obstacles if there is a collide.
        hit_sound.play()
        enemy_group.sprites()[0].kill()
        lives -= 1
    lives_surf = test_font.render(f'Lives: {lives}',False,(64,64,64))
    lives_rect = lives_surf.get_rect(center = (100,50))
    screen.blit(lives_surf,lives_rect)
    return lives
          
    
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (900,50))
    screen.blit(score_surf,score_rect)
    return current_time
        
# =============================================================================
# Pygame Technical stuff
# =============================================================================

pygame.init()

# screen
screen = pygame.display.set_mode((1000,750))

# screen name
pygame.display.set_caption('Dinosaur Run')

# font for text
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# clock for the frame rate

clock = pygame.time.Clock()

# game state

game_state = False

start_time = 0

score = 0

game_lives = 3

# =============================================================================
# Music
# =============================================================================

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.5)

hit_sound = pygame.mixer.Sound("audio/hitsound.wav")
hit_sound.set_volume(0.5)

end_game_music = pygame.mixer.Sound("audio/game-over-mono.wav")
end_game_music.set_volume(0.5)

# =============================================================================
# Backgroud Surfaces
# =============================================================================


# idle dinosaur 

idle_1 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (1).png"),0,0.7).convert_alpha()
idle_2 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (2).png"),0,0.7).convert_alpha()
idle_3 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (3).png"),0,0.7).convert_alpha()
idle_4 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (4).png"),0,0.7).convert_alpha()
idle_5 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (5).png"),0,0.7).convert_alpha()
idle_6 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (6).png"),0,0.7).convert_alpha()
idle_7 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (7).png"),0,0.7).convert_alpha()
idle_8 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (8).png"),0,0.7).convert_alpha()
idle_9 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (9).png"),0,0.7).convert_alpha()
idle_10 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Idle (10).png"),0,0.7).convert_alpha()

        
idle_surface_list = [idle_1, idle_2, idle_3, idle_4, idle_5, idle_6, idle_7, idle_8, idle_9]

idle_frame_index =  0     
idle_surf = idle_surface_list[idle_frame_index]
idle_rect = idle_surf.get_rect(midbottom = (570,540))


# dead dinosaur


dead_1 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (1).png"),0,0.7).convert_alpha()
dead_2 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (2).png"),0,0.7).convert_alpha()
dead_3 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (3).png"),0,0.7).convert_alpha()
dead_4 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (4).png"),0,0.7).convert_alpha()
dead_5 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (5).png"),0,0.7).convert_alpha()
dead_6 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (6).png"),0,0.7).convert_alpha()
dead_7 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (7).png"),0,0.7).convert_alpha()
dead_8 = pygame.transform.rotozoom(pygame.image.load("Graphics/dinosaur/Dead (8).png"),0,0.7).convert_alpha()
     
dead_surface_list = [dead_1, dead_2, dead_3, dead_4, dead_5, dead_6, dead_7, dead_8]

dead_frame_index =  0     
dead_surf = dead_surface_list[dead_frame_index]
dead_rect = dead_surf.get_rect(midbottom = (470,480))



# background

backgroud_surface = pygame.image.load("Graphics/background/BG.png").convert()

# floor 

floor_surface = pygame.image.load("Graphics/background/floor.png").convert()

# name of the game

name_surf = pygame.transform.rotozoom(test_font.render("Dinosaur Run",False,(64,64,64)), 0,1.4)
name_rect = name_surf.get_rect(center = (500,140))

# instructions

ins_surf = pygame.transform.rotozoom(test_font.render("Press Start to Play",False,(64,64,64)), 0,1.4)
ins_rect = ins_surf.get_rect(center = (500,610))


# =============================================================================
# Sprite Groups
# =============================================================================

# creating the player sprite
dinosaur = pygame.sprite.GroupSingle()
dinosaur.add(Dinosaur())

# creating the enemies sprytes

enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy())

# =============================================================================
# Timers
# =============================================================================

enemy_timer = pygame.USEREVENT + 1

pygame.time.set_timer(enemy_timer,randint(1800,2000))

# =============================================================================
# ################################## Run Game ##############################
# =============================================================================

# =============================================================================
# While true and events
# =============================================================================

while True:
    # to be able to quit de game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_state:    
            if event.type == enemy_timer:
                enemy_group.add(Enemy())
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = True
                start_time = int(pygame.time.get_ticks() / 1000)
                dead_frame_index = 0
            
# =============================================================================
# Game
# =============================================================================

    
    if game_state:
        
        screen.blit(backgroud_surface, (0,0))  
        screen.blit(floor_surface, (0,610))
       
    
        dinosaur.draw(screen)
        dinosaur.update()
    
        enemy_group.draw(screen)
        enemy_group.update()
        
        game_lives = collision_sprite()
        
        score = display_score()
        
        if game_lives == 0:
            enemy_group.empty()
            game_state = False
            game_lives = 3
        
        
        
        
    else:
        
        if score == 0:
            screen.fill((167, 244, 223))
            screen.blit(name_surf, name_rect)
            screen.blit(ins_surf, ins_rect)
            screen.blit(idle_surf, idle_rect)
            animate_idle()
            
        else: 
            screen.fill((167, 244, 223))
            screen.blit(name_surf, name_rect)
            final_score_surf = pygame.transform.rotozoom(test_font.render(f'Your score was: {score}',False,(64,64,64)), 0,1.4)
            final_score_rect = final_score_surf.get_rect(center = (500,610))
            screen.blit(final_score_surf, final_score_rect)
            screen.blit(dead_surf, dead_rect)
            animate_dead()
    
            
# =============================================================================
# Final Stuff
# =============================================================================

    pygame.display.update()
    clock.tick(60)