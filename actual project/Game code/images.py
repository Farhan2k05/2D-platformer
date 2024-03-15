import pygame
from Text import *
#backgrounds
menu_bg=pygame.image.load("designs\BG\main_menu.jpg")
menu_bg=pygame.transform.scale(menu_bg,(window_width,window_height))
lv1_bg=pygame.image.load("designs\BG\mountains.jpg")
lv1_bg=pygame.transform.scale(lv1_bg,(window_width,window_height))
lv2_bg=pygame.image.load("designs\BG\desert.jpg")
lv2_bg=pygame.transform.scale(lv2_bg,(window_width,window_height))
lv3_bg=pygame.image.load("designs\BG\winter.jpg")
lv3_bg=pygame.transform.scale(lv3_bg,(window_width,window_height))

#platforms:
grass=pygame.image.load("designs\platforms\grass.png")
grass=pygame.transform.scale(grass,(64,64))
dirt=pygame.image.load("designs\platforms\dirt.png")
dirt=pygame.transform.scale(dirt,(64,64))
block=pygame.image.load("designs\platforms\Block.png")
block=pygame.transform.scale(block,(64,64))
jump_block=pygame.image.load("designs\platforms\jump_block.png")
jump_block=pygame.transform.scale(jump_block,(64,64))
fast_block=pygame.image.load("designs\platforms\Fast_block.png")
fast_block=pygame.transform.scale(fast_block,(64,64))
slow_block=pygame.image.load("designs\platforms\slow_block.png")
slow_block=pygame.transform.scale(slow_block,(64,64))
target_block=pygame.image.load("designs\platforms\end.png")
target_block=pygame.transform.scale(target_block,(64,64))
#monster
monster_image=pygame.image.load("designs\monster\monster.png")
monster_image=pygame.transform.scale(monster_image,(64,48))

#player
player_base=pygame.image.load("designs\player\player_base.png")
player_base_right=pygame.transform.scale(player_base,(55,68))
player_base_left=pygame.transform.flip(player_base_right,True,False)

player_jump=pygame.image.load("designs\player\player_jump.png")
player_jump_right=pygame.transform.scale(player_jump,(51,68))
player_jump_left=pygame.transform.flip(player_jump_right,True,False)

player_fall=pygame.image.load("designs\player\player_fall.png")
player_fall_right=pygame.transform.scale(player_fall,(51,68))
player_fall_left=pygame.transform.flip(player_fall_right,True,False)

player_walk1=pygame.image.load("designs\player\walk1.png")
player_walk1_right=pygame.transform.scale(player_walk1,(51,68))
player_walk1_left=pygame.transform.flip(player_walk1_right,True,False)

player_walk2=pygame.image.load("designs\player\walk2.png")
player_walk2_right=pygame.transform.scale(player_walk1,(51,68))
player_walk2_left=pygame.transform.flip(player_walk2_right,True,False)

player_walk3=pygame.image.load("designs\player\walk3.png")
player_walk3_right=pygame.transform.scale(player_walk3,(51,68))
player_walk3_left=pygame.transform.flip(player_walk3_right,True,False)

#KEYS
space_key=pygame.image.load("designs\KEYS\SPACE_BAR.png")
space_key=pygame.transform.scale(space_key,(500,68))
w_key=pygame.image.load("designs\KEYS\W_KEY.png")
w_key=pygame.transform.scale(w_key,(80,68))
up_arrow_key=pygame.image.load("designs\\KEYS\\UP_ARROW.png")
up_arrow_key=pygame.transform.scale(up_arrow_key,(80,68))

left_key=pygame.image.load("designs\KEYS\LEFT_ARROW.png")
left_key=pygame.transform.scale(left_key,(80,68))
a_key=pygame.image.load("designs\KEYS\A_KEY.png")
a_key=pygame.transform.scale(a_key,(80,68))

right_key=pygame.image.load("designs\KEYS\RIGHT_ARROW.png")
right_key=pygame.transform.scale(right_key,(80,68))
d_key=pygame.image.load("designs\KEYS\D_KEY.png")
d_key=pygame.transform.scale(d_key,(80,68))


walk_list_right=[player_base_right,player_walk1_right,player_walk2_right,player_walk3_right]
walk_list_left=[player_base_left,player_walk1_left,player_walk2_left,player_walk3_left]



