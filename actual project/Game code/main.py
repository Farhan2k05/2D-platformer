import pygame , sys
from Text import *
from Time_scores import *
from Level_layouts import *
from images import *
pygame.init()
pygame.display.set_caption("Amazing_Game")
clock = pygame.time.Clock()
#background music
music = pygame.mixer.Sound("audio\wounderous water.mp3")
music.play(loops = -1)


class Level():

    def __init__(self,level_map1):# generates tiles with coordinates matching the location of the digits in the level map
        # lists of tiles
        self.tiles_list = []    
        self.monsters_list = []

        #moving tiles 
        self.goUp=True
        self.goDown=False
        self.count=0
        self.step = 1
        self.angle = 0

        #monster
        self.monster_left_lock = False
        self.monster_right_lock = False

        self.monster_velocity = pygame.math.Vector2(0,0)
        self.monster_velocity.x =1
        self.monster_speed = 5

        #terrain generation
        row_no= 0
        for row in level_map1:
            column_no=0
            for tile in row:
                if tile!=0:
                    tile_surf = pygame.Surface([64,64]).convert_alpha()
                    tile_rect = tile_surf.get_rect()
                    tile_rect.x = column_no * 64
                    tile_rect.y = row_no * 64

                    if tile==1:
                        tile_surf=grass
                        tile = (tile_surf,tile_rect,"immobile")
                    if tile==2:
                        tile_surf=dirt
                        tile = (tile_surf,tile_rect,"immobile")
                    elif tile==3:
                        tile_surf=block
                        tile = (tile_surf,tile_rect,"up_down")
                    elif tile==4:
                        tile_surf.fill("purple")
                        tile = (tile_surf,tile_rect,"rotating")                  
                    elif tile==5:
                        tile_surf=fast_block
                        tile = (tile_surf,tile_rect,"fast")
                    elif tile==6:
                        tile_surf=slow_block
                        tile = (tile_surf,tile_rect,"slow")            
                    elif tile==7:
                        tile_surf=jump_block
                        tile = (tile_surf,tile_rect,"jumpy_tile")
                    elif tile==8:
                        tile_surf=monster_image
                        tile_rect.y+=16
                        tile = (tile_surf,tile_rect,"monster")
                        self.monsters_list.append(tile)
                    elif tile==9:
                        tile_surf=target_block
                        tile = (tile_surf,tile_rect,"target")
                        
                    if tile[2]!="monster":
                        self.tiles_list.append(tile)

                                   
                column_no +=1
            row_no +=1
        
        #camera modes
        self.camera_lock_left = False
        self.camera_lock_right = False

    def display_terrain(self):
        #goes through list containing all the platforms surfaces and rectangles and displays them
        for tile in self.tiles_list:
            if tile[2]!="rotating":
                window.blit(tile[0],tile[1])
        for tile in self.monsters_list:
            window.blit(tile[0],tile[1])
                    
    def camera(self):
        
        if player.rect.x<=300:
            player.rect.x+=10
        if player.rect.x < window_width/4 :#check to see if player is on the left quarter of the screen
            self.camera_lock_left=True
        elif player.rect.x > window_width*0.6: #check to see if player is on the right side of the screen
            self.camera_lock_right = True
        else:
            self.camera_lock_left = False #if player is around the middle of the screen camera is still.
            self.camera_lock_right = False
        
        #monster moves with the rest of the tiles when everything is shifting
        if self.camera_lock_right == True and pygame.key.get_pressed()[pygame.K_d or pygame.K_RIGHT]:
            for monster in self.monsters_list:
                monster[1].x -= 8
            for tile in self.tiles_list:
                    tile[1].x -= 8
        elif self.camera_lock_left == True and pygame.key.get_pressed()[pygame.K_a or pygame.K_LEFT]:
            for monster in self.monsters_list:
                monster[1].x += 8
            for tile in self.tiles_list:
                    tile[1].x += 8
        
        
    def moving_tiles(self):
        #continous loop where count variable is continuasly incremented or decremented
        # when count is incrmented block goes up and viceversa when count is decremented.
        #Count begins to increment/decrement when a maginutde of 100 is reached.
        for tile in self.tiles_list:
            if tile[2]=="up_down":
                if self.goUp:
                    tile[1].y -=1
                    self.count +=1
                elif self.goDown:
                    tile[1].y +=1
                    self.count-=1
                if self.count ==100:
                    self.goUp=False
                    self.goDown=True
                elif self.count==-100:
                    self.goDown=False
                    self.goUp=True

            # if tile[2]=="rotating":
            #     tile = list(tile)
            #     self.angle +=1
            #     pos = tile[1].center
            #     tile[0] = pygame.transform.rotozoom(tile[0],self.angle,1).convert_alpha()
            #     tile[1] = tile[0].get_rect(center=pos)


            #     tile = tuple(tile)
            #     window.blit(tile[0],tile[1])
    
    def monsters(self): 
         #monster x coordinates constantly incremneted/decremented to reach player.
        for monster in self.monsters_list:
                monster_rect=monster[1]
                if (player.rect.centerx < monster_rect.centerx):
                    self.monster_velocity =-1
                elif (player.rect.centerx > monster_rect.centerx):
                    self.monster_velocity=1
                else:
                    self.monster_velocity = 0 #monster remains still if player is in the same x coordinates.
                monster_rect.x += self.monster_velocity*self.monster_speed
    
    def keep_monster_ground(self):
        #monster stops moving when 1 tile away from leaving the current platform
        #There to prevent monster leaving platform causing it to virtually fly
        for monster in self.monsters_list:            
            collision_count=0
            for tile in self.tiles_list :
                block=tile[1]
                monster_rect = monster[1]
                if block.colliderect(monster_rect.x+self.monster_velocity*127,monster_rect.y+1,64,64):
                    collision_count +=1
            if collision_count == 0:
                self.monster_speed=0
            else:
                self.monster_speed =5

    def update(self):
        # runs all methods under the player class
        self.monsters()
        self.keep_monster_ground()
        self.moving_tiles()
        self.display_terrain()
        self.camera()
        
class Player():
    def __init__(self,x,y):
        #player model
        self.surf = pygame.Surface([45,60])
        self.surf=player_base_right.convert_alpha()
        self.rect = self.surf.get_rect()

        #position
        self.rect.x = x
        self.rect.y = y
        
        #player states
        self.player_on_ground = False
        self.jumpy = False
        self.fast = False
        self.slow = False
        self.direction=""
        self.player_base=player_base_right

        self.vector = pygame.math.Vector2(0,0) 

        #horizontal motion
        self.vector.y = 1
        self.gravity = 0.5
        self.jump_speed = -20

        #vertical motion
        self.acceleration = 0.8
        self.speed_limit =4   

        self.width = self.surf.get_width()
        self.height = self.surf.get_height()

        self.count=0

    def get_input(self):
        key = pygame.key.get_pressed()#shortened command to detect key press
        
        #checks for space press, reverses playher gravity and sets player on ground variable to false
        if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) and self.vector.y ==0:
            if self.player_base==player_base_right:
                self.surf=player_jump_right
            else:
                self.surf=player_base_left
            self.player_on_ground = False
            self.vector.y = self.jump_speed
            self.gravity =1.45

        # checks for key presses that let player move left or right
        if (key[pygame.K_d] or key[pygame.K_RIGHT]):
            self.count+=1
            self.player_base=player_base_right
            if level.camera_lock_right == False:
                self.vector.x += self.acceleration
                if self.vector.x < -self.speed_limit :
                    self.vector.x = -self.speed_limit
        elif (key[pygame.K_a] or key[pygame.K_LEFT]):
            self.count+=1
            self.player_base=player_base_left
            if level.camera_lock_left == False:
                self.vector.x -= self.acceleration
                if self.vector.x > self.speed_limit:
                    self.vector.x = self.speed_limit       
        else: #if no key is pressed player has no vertical velocity
            self.vector.x =0
            self.direction="none"
        
        self.rect.x += self.vector.x
             
    def collisions(self):       
        for tile in level.tiles_list:
            block=tile[1]
            #verticl collisions
            if block.colliderect(self.rect.x,self.rect.y +self.vector.y ,self.width,self.height):
                    self.player_on_ground = True
                    if self.vector.y >= 0:
                        self.rect.bottom = block.top
                    else: self.rect.top = block.bottom
                    self.vector.y =0
                    self.gravity =0

                    #special tiles and target block
                    #if player collides with a special tile their state is changed
                    
                    if tile [2] == "jumpy_tile":
                        self.jumpy = True
                    else: self.jumpy=False 
                    if tile[2] =="fast":
                        self.fast=True
                    else: self.fast = False
                    if tile[2] =="slow":
                        self.slow = True
                    else: self.slow = False
                    if tile[2] == "target":#if player touches target block they are teleported really high up
                        self.rect.y=-10000            
            #horizontal collisions
            #player cant move towards a block if they are colliding with it
            if tile[2] == "immobile" or tile[2]=="jumpy_tile" or tile[2]=="fast" or tile[2]=="slow" or tile[2]=="up_down":
                if block.colliderect(self.rect.x +self.vector.x,self.rect.y,self.width,self.height):
                    self.vector.x =0
        #monster collision
        #player gets teleported really down when monster is in contact with player
        for monster in level.monsters_list:
            if monster[1].colliderect(self.rect):
                self.rect.y=10000
                                   
    def collision_checker(self):
        #if the player is said to be standing on ground and they are not colliding with anything
        # the player gravity is incremented as evidently they are not touching the ground
        if self.player_on_ground:
            collision_count =0
            for tile in level.tiles_list :
                block=tile[1]
                if block.colliderect(self.rect.x,self.rect.y +self.vector.y ,self.width,self.height):
                    collision_count +=1
                    break
            if collision_count == 0:
                self.vector.y = 2
                self.gravity = 4

    def apply_gravity(self):
        #constantly changes player vertical position according to its gravity(acceleration) and velocity
        self.vector.y += self.gravity
        if self.vector.y > 8:
            self.vector.y = 8
        self.rect.y += self.vector.y

    def tile_buffs(self):
        #changes player characteristics depending on what state they are in
        if self.jumpy==True:
            self.jump_speed = -27
        else: self.jump_speed = -22.5
        
        if self.fast ==True or self.slow == True:
            if self.fast ==True:                   
                self.acceleration = 0.8
                self.speed_limit = 8
            if self.slow ==True:
                self.acceleration = 0.2
                self.speed_limit = 0.2
        else: 
            self.acceleration = 0.4
            self.speed_limit=4
    
    def animation(self):
        if self.vector==(0,0):#player image set to default one when stationary
            self.surf=self.player_base   
        #when teh count goes up count is incremeneted(lines 236 and 243) as count changes played image changes.   
        if self.count>=30:
            self.count=0
        if self.vector.y==0 and (self.vector.x>0 or level.camera_lock_right):
            self.surf=walk_list_right[int((self.count)/10)]
        elif self.vector.y==0 and (self.vector.x<0 or level.camera_lock_left):
            self.surf=walk_list_left[int((self.count)/10)]  
        
    def update(self):#runs all methods in the desired order in one go        
        self.apply_gravity()
        self.get_input()
        self.animation()
        self.collision_checker()
        self.collisions()
        self.tile_buffs()
        
        window.blit(self.surf,self.rect)

#calculates time player has been in the level by finding the difference between the game run time when game started and current time
def timer():
    time= Text(25,25,25,"",str("Time "+str(current_time)))#create a text object
    window.blit(time.text_surface,time.rect)#displayes time
    return current_time

xtime=0 #A variable that stores the total run time of game before we start each level.
run_time=0 #stores run time for  current level
paused_time=0
paused_time_Start=0
previous_paused_time=0

player = Player((window_width/4)+20,700)
level=Level(level_map1)

#Game states
game_state = "main_menu"
current_level=""



def window_():#keeps game running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)

#main game loop where different objects and things are displayed depending on the 
#current game state. 
while True:#main game loop 
    if game_state=="Levels":
        window_()
        window.fill("white")
        window.blit(back_button.text_surface,back_button.rect)
        window.blit(level1_button.text_surface,level1_button.rect)
        window.blit(level2_button.text_surface,level2_button.rect)
        window.blit(level3_button.text_surface,level3_button.rect)
        window.blit(level1_time.text_surface,level1_time.rect)
        window.blit(level2_time.text_surface,level2_time.rect)
        window.blit(level3_time.text_surface,level3_time.rect)
        window.blit(levels_title.text_surface,levels_title.rect)
        window.blit(best_runs.text_surface,best_runs.rect)
        current_time=0
       
    elif game_state=="Level 1" or game_state=="Level 2" or game_state=="Level 3":
        window_()

        current_level=game_state
        if pygame.key.get_pressed()[pygame.K_p]:
            paused_time_Start=(pygame.time.get_ticks()/1000)
            game_state="pause"
        if player.rect.y > 1000:
            game_state="game over"
        if player.rect.y<-1000:
            run_time=int(pygame.time.get_ticks()/1000)-xtime-paused_time
            best_times=get_best_times()#retrieves a list containing the best run times
            # if new best time is acheived a string is created contaning the 2 scores
            if current_level=="Level 1" and run_time< int(best_times[0]):
                new_best_times=str(run_time)+" "+ best_times[1]+" "+ best_times[2]
            elif current_level=="Level 2" and run_time< int(best_times[1]):
                new_best_times=best_times[0]+" "+str(run_time)+" "+best_times[2]
            elif current_level=="Level 3" and run_time< int(best_times[2]):
                new_best_times=best_times[0]+" "+best_times[1]+" "+str(run_time)
            else: new_best_times=best_times[0]+" "+best_times[1]+" "+best_times[2]
            set_new_best_times(str(new_best_times))#the best run times are saved in the file
            game_state="Level complete"
        if game_state=="Level 1": window.blit(lv1_bg,(0,0))
        elif game_state=="Level 2": window.blit(lv2_bg,(0,0))
        elif game_state=="Level 3": window.blit(lv3_bg,(0,0))
        window.blit(pause_button.text_surface,pause_button.rect)
        

        level.update()
        player.update()
        timer()
    elif game_state=="main_menu":
        window_()
        window.blit(menu_bg,(0,0))
        window.blit(controls_button.text_surface,controls_button.rect)
        window.blit(levels_button.text_surface,levels_button.rect)
        window.blit(exit_button.text_surface,exit_button.rect)
    elif game_state=="game over":
        window_()
        window.fill("white")
        window.blit(game_over_title.text_surface,game_over_title.rect)
        window.blit(restart_button.text_surface,restart_button.rect)
        window.blit(main_menu_button.text_surface,main_menu_button.rect)
    elif game_state=="Level complete":
        paused_time=0
        current_time=0
        window_()
        window.fill("white")
        # depending on what level the player was in when completed, the button to go the next level is displayed
        if current_level=="Level 1":
            level2_button.rect.center=(window_width*0.225,window_height*0.574)
            window.blit(level2_button.text_surface,level2_button.rect)
        elif current_level=="Level 2":
            level3_button.rect.center=(window_width*0.225,window_height*0.574)
            window.blit(level3_button.text_surface,level3_button.rect)
        window.blit(level_complete.text_surface,level_complete.rect)
        window.blit(main_menu_button.text_surface,main_menu_button.rect)
    elif game_state=="controls":
        window_()
        window.fill("white")
        window.blit(back_button.text_surface,back_button.rect)
        window.blit(space_key,(controls1.rect.x+200,controls1.rect.y-10))
        window.blit(w_key,(controls1.rect.x+710,controls1.rect.y-12))
        window.blit(up_arrow_key,(controls1.rect.x+800,controls1.rect.y-12))
        window.blit(left_key,(controls2.rect.x+260,controls2.rect.y-10))
        window.blit(a_key,(controls2.rect.x+170,controls2.rect.y-10))
        window.blit(right_key,(controls3.rect.x+330,controls3.rect.y-10))
        window.blit(d_key,(controls3.rect.x+240,controls3.rect.y-10))
        window.blit(controls1.text_surface,controls1.rect)
        window.blit(controls2.text_surface,controls2.rect)    
        window.blit(controls3.text_surface,controls3.rect)         
    elif game_state=="pause":
        window_()
        window.fill("white")
        paused_time=int((pygame.time.get_ticks()/1000)-paused_time_Start)+previous_paused_time
        window.blit(pause_title.text_surface,pause_title.rect)
        window.blit(main_menu_button.text_surface,main_menu_button.rect)
        window.blit(resume_button.text_surface,resume_button.rect)
    for button in button_array: # loops between every button a checks for button clicks and redirects the player to the corresponding section.
        mouse_cordinates = pygame.mouse.get_pos()
        if button.rect.collidepoint(mouse_cordinates):
            button.resize(100)
            if pygame.mouse.get_pressed()[0] :
                if game_state=="Levels":
                    if button.action=="Level 1":
                        xtime=int(pygame.time.get_ticks()/1000)
                        level=Level(level_map1)
                    elif button.action=="Level 2":
                        xtime=int(pygame.time.get_ticks()/1000)
                        level=Level(level_map2)
                    elif button.action=="Level 3":
                        xtime=int(pygame.time.get_ticks()/1000)
                        level=Level(level_map3)
                    game_state=button.action
                    player.rect.center=((window_width/4)+30,700)                 
                elif game_state=="game over":
                    if button.action=="restart":
                        game_state=current_level
                        if current_level=="Level 1":
                            level=Level(level_map1)
                        elif current_level=="Level 2":
                            level=Level(level_map2)
                        elif current_level=="Level 3":
                            level=Level(level_map3)
                        xtime=int(pygame.time.get_ticks()/1000)
                        player.rect.center=((window_width/4)+20,700)
                    elif button.action=="main_menu":
                            game_state="main_menu"
                elif game_state=="Level complete":
                    if current_level=="Level 1" and button.action=="Level 2":
                        xtime=int(pygame.time.get_ticks()/1000)
                        level=Level(level_map2) 
                        player.rect.center=(100,100)
                        game_state="Level 2"         
                    elif current_level=="Level 2" and button.action=="Level 3":
                        xtime=int(pygame.time.get_ticks()/1000)
                        player.rect.center=(100,100)
                        game_state="Level 3"
                        level=Level(level_map3)
                    elif button.action=="main_menu":
                        game_state="main_menu"                     
                elif game_state=="controls":
                    if button.action=="main_menu":
                        game_state="main_menu"
                elif game_state=="main_menu":
                    if button.action=="Levels":
                        level2_button.rect.topleft=(window_width*0.15,window_height*0.5)
                        level3_button.rect.topleft=(window_width*0.15,window_height*0.7)
                        level1_time=Text(window_width*0.6,window_height*0.3,50,"None",(get_best_times())[0])
                        level2_time=Text(window_width*0.6,window_height*0.5,50,"None",(get_best_times())[1])
                        level3_time=Text(window_width*0.6,window_height*0.7,50,"None",(get_best_times())[2])
                        game_state=button.action
                    if button.action=="controls":
                        game_state=button.action
                    elif button.action=="exit":
                        exit()
                elif game_state=="Level 1" or game_state=="Level 2" or game_state=="Level 3":
                    if button.action=="pause":
                        paused_time_Start=(pygame.time.get_ticks()/1000)
                        game_state="pause"
                elif game_state=="pause":
                    
                    if button.action=="main_menu":
                        game_state="main_menu"
                    if button.action=="resume":
                        previous_paused_time=paused_time
                        game_state=current_level
                    
        else:
            button.resize(50)
          
                    

