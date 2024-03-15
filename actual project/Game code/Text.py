import pygame , sys
from Time_scores import *
pygame.init()
#window=pygame.display.set_mode((1200,750),pygame.RESIZABLE)
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
window_height = window.get_height()
window_width = window.get_width()

class Text():# creates a piece of text which has a rectangle and has a action attiribute
    def __init__(self,x,y,size,action,text):
        self.text=text
        myFont= pygame.font.Font("font/MIDNSBRG.ttf",size)
        self.text_surface=myFont.render((text),False,("black"))
        self.rect = self.text_surface.get_rect(center=(x,y))
        self.rect.x =x
        self.rect.y =y
        self.action=action
        self.size=size
    
    def resize(self,size):#takes in number and changes the objects dimensions
        self.font= pygame.font.Font("font/MIDNSBRG.ttf",size)
        self.text_surface=(self.font).render((self.text),False,("black"))
        self.rect = self.text_surface.get_rect(center=(self.rect.centerx,self.rect.centery))


#buttons
levels_button=Text(window_width*0.42,window_height*0.4,50,"Levels","Levels")
level1_button=Text(window_width*0.15,window_height*0.3,50,"Level 1","Level 1")
level2_button=Text(window_width*0.15,window_height*0.5,50,"Level 2","Level 2")
level3_button=Text(window_width*0.15,window_height*0.7,50,"Level 3","Level 3")
restart_button=Text(window_width/5,window_height*0.55,50,"restart","Restart")
main_menu_button=Text(window_width/(5/3)+30,window_height*0.55,50,"main_menu","Main Menu")
exit_button=Text(window_width*0.45,window_height*0.7,50,"exit","exit")
pause_button=Text(window_width*0.45,window_height*0.7,50,"exit","exit")
controls_button=Text(window_width*0.38,window_height*0.55,50,"controls","controls")
back_button=Text(window_width*0.025,window_height*0.025,50,"main_menu","<--")
pause_button=Text(window_width*0.95,window_height*0.05,50,"pause","P")
resume_button=Text(window_width/5,window_height*0.55,50,"resume","Resume")

button_array=[levels_button,exit_button,level1_button,level2_button,level3_button,restart_button,main_menu_button,controls_button,back_button,pause_button,resume_button]

  

#Titles:
game_over_title=Text(window_width*0.125,window_height*0.15,150,"none","Game Over!")
level_complete=Text(window_width*0.125,window_height*0.15,100,"none","Level completed!")
levels_title=Text(window_width*0.1,window_height*0.1,60,"none","Levels :")
best_runs=game_over=Text(window_width*0.55,window_height*0.1,60,"none","Best runs:")
pause_title=Text(window_width*0.3075,window_height*0.15,150,"none","PAUSE")

#controls:
controls1=Text(window_width*0.05,window_height*0.35,50,"none","JUMP-")
controls2=Text(window_width*0.05,window_height*0.5,50,"none","LEFT-")
controls3=Text(window_width*0.05,window_height*0.65,50,"none","RIGHT-")

