#===載入套件開始
from lib2to3.pygram import python_grammar_no_print_statement
from time import time
from time import sleep
import pygame 
import sys 
import os 
os.chdir(sys.path[0])
from pygame.locals import *
import math
import random
#***載入套件結束***

#===初始化設定開始===
LIMIT_LOW=140
LIMIT_HIGH=140
pygame.init()
timer=0
clock=pygame.time.Clock()
stuff=2
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,0,255)
brown=(60,40,20)
black=(0,0,0)
#***初始化設定結束***



#===載入圖片開始===
img=pygame.image.load("image/bg.png")
img_dinosaur=[pygame.image.load("image/小恐龍1.png"),pygame.image.load("image/小恐龍2.png")]
img_cacti=pygame.image.load("image/cacti.png")
img_teacher=pygame.image.load("image/teacher.png")
img_teacher1=pygame.image.load("image/teacher1.png")
img_teacher2=pygame.image.load("image/teacher2.png")
img_gg=pygame.image.load("image/gameover.png")
img_ptera=[pygame.image.load("image/翼龍飛飛1.png"),pygame.image.load("image/翼龍飛飛2.png")]
img_godown=[pygame.image.load("image/小恐龍蹲下1.png"),pygame.image.load("image/小恐龍蹲下2.png")]
#***載入圖片結束***


#===遊戲視窗設定開始===
bg_x=img.get_width()
bg_y=img.get_height()
bg_size=(bg_x,bg_y+500)
roll_x=0

pygame.display.set_caption("Dinosaur")
screen=pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***


#===分數設定開始===
score=0
typeface=pygame.font.get_default_font()
score_font=pygame.font.Font(typeface,36)

def get_score(win):
    global score

    score_sur=score_font.render(str(score),True,red)
    win.blit(score_sur,[10,10])
#***分數設定結束***


#===恐龍設定開始===
dino_show=img_dinosaur
dino_limit=LIMIT_LOW
ds_x=50
ds_y=dino_limit
jumpState=False
jumpValue=0
def get_dino_limit(dino_img):
    return bg_y-100-dino_img[0].get_height()
def move_dinosaur(win,timer):
    global ds_x, ds_y,jumpState,jumpValue
    if jumpState:
        if ds_y>=LIMIT_LOW:
            jumpValue=-15
            pygame.mixer.music.load("image/button03a.mp3")
            pygame.mixer.music.play()
        if ds_y<=0:
            jumpValue=15
        ds_y+=jumpValue
        if ds_y>=LIMIT_LOW:
            jumpState=False
    win.blit(dino_show[timer%20//10],[ds_x,ds_y])
#***恐龍設定結束***

#===仙人掌設定開始===
cacti_h=img_cacti.get_height()
cacti_x=bg_x-100
cacti_y=LIMIT_LOW
cacti_shift=10
cacti_dist=int((cacti_h+cacti_h)/2)
def move_cacti(win):
    global cacti_x,cacti_y,cacti_shift,score
    global score
    global stuff
    cacti_x-=cacti_shift
    win.blit(img_cacti,[cacti_x,cacti_y])
    if (cacti_x<0):
        stuff=random.randint(0,4)
        score+=1
        cacti_x=bg_x-10
        cacti_y=LIMIT_LOW

#***仙人掌設定結束***

#===老師設定開始===#
teacher_h=img_teacher.get_height()
teacher_x=bg_x-100
teacher_y=LIMIT_LOW
teacher_shift=10
teacher_dist=int((teacher_h+teacher_h)/2)
def move_teacher(win):
    global teacher_x,teacher_y,teacher_shift,score
    global score
    global stuff
    teacher_x-=teacher_shift
    win.blit(img_teacher,[teacher_x,teacher_y])
    if (teacher_x<0):
        stuff=random.randint(0,4)
        score+=1
        teacher_x=bg_x-300
        teacher_y=LIMIT_LOW
#***老師設定結束***#

#===老師1設定開始===#
teacher1_h=img_teacher1.get_height()
teacher1_x=bg_x-100
teacher1_y=LIMIT_LOW+20
teacher1_shift=10
teacher1_dist=int((teacher1_h+teacher1_h)/2)
def move_teacher1(win):
    global teacher1_x,teacher1_y,teacher1_shift,score
    global score
    global stuff
    teacher1_x-=teacher1_shift
    win.blit(img_teacher1,[teacher1_x,teacher1_y])
    if (teacher1_x<0):
        stuff=random.randint(0,4)
        score+=1
        teacher1_x=bg_x-300
        teacher1_y=LIMIT_LOW+20
#***老師1設定結束***#

#===老師2設定開始===#
teacher2_h=img_teacher2.get_height()
teacher2_x=bg_x-100
teacher2_y=LIMIT_LOW
teacher2_shift=10
teacher2_dist=int((teacher2_h+teacher2_h)/2)
def move_teacher2(win):
    global teacher2_x,teacher2_y,teacher2_shift,score
    global score
    global stuff
    teacher2_x-=teacher2_shift
    win.blit(img_teacher2,[teacher2_x,teacher2_y])
    if (teacher2_x<0):
        stuff=random.randint(0,4)
        score+=1
        teacher2_x=bg_x-300
        teacher2_y=LIMIT_LOW
#***老師2設定結束***#

#===翼龍設定開始===
ptera_w=img_ptera[0].get_width()
ptera_h=img_ptera[0].get_height()
ptera_x=bg_x-200
ptera_y=LIMIT_LOW-30
ptera_shift=10
ptera_dist=int((ptera_w+ptera_h)/2)
def move_ptera(win,timer):
    global ptera_x,ptera_y,ptera_shift,score
    global stuff
    ptera_x-=ptera_shift
    if (ptera_x<0):
        stuff=random.randint(0,4)
        score+=1
        ptera_x=bg_x-100
        ptera_y=LIMIT_LOW-30
    win.blit(img_ptera[timer%20//10],[ptera_x,ptera_y])
#***翼龍設定結束***

#***碰撞設定開始***
def is_hit(x1,y1,x2,y2,r):
    if ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))<(r*r):
        pygame.mixer.music.load("image/blip03.mp3") 
        pygame.mixer.music.play(2)
        return True
    else:
        return False
#***碰撞設定結束***

#===GameOver設定開始===
gg=False
gg_w=img_gg.get_width()
gg_h=img_gg.get_height()

def game_over(win):
    win.blit(img_gg,((bg_x-gg_h)/2,(bg_y-gg_h)/2))
#***GameOver設定結束***

#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(25)
    timer+=1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP and ds_y>=dino_limit:
                jumpState=True
            elif event.key==K_DOWN and jumpState==False:
                dino_show=img_godown
                dino_limit=get_dino_limit(dino_show)
                ds_y=dino_limit
            elif event.key==K_RETURN and gg==True:
                gg=False
                cacti_x=bg_x-100
                ptera_x=bg_x-100
                teacher_x=bg_x-100
                teacher1_x=bg_x-100
                teacher2_x=bg_x-100
                ds_x=50
                ds_y=LIMIT_LOW
                score=0
                jumpState=False
        elif event.type==KEYUP:
            if event.key==K_DOWN and jumpState==False:
                dino_show=img_dinosaur
                dino_limit=get_dino_limit(dino_show)
                ds_y=dino_limit
    if gg==True:
    #===遊戲結束===       
        game_over(screen)
    else:
        #===遊戲進行===        
        
        roll_x=(roll_x-7) % bg_x
        screen.blit(img,[roll_x-bg_x,0])
        screen.blit(img,[roll_x,0])

        #===更新角色狀態===
        move_dinosaur(screen,timer)
        if stuff==0:
            move_cacti(screen)
        if stuff==1:
            move_ptera(screen,timer)
        if stuff==2:
            move_teacher(screen)
        if stuff==3:
            move_teacher1(screen)
        if stuff==4:
            move_teacher2(screen)
        
        get_score(screen)
        if (is_hit(ds_x,ds_y,cacti_x,cacti_y,cacti_dist)):
            gg=True
        if (is_hit(ds_x,ds_y,ptera_x,ptera_y,ptera_dist)):
            gg=True
        if (is_hit(ds_x,ds_y,teacher_x,teacher_y,teacher_dist)):
            gg=True
        if (is_hit(ds_x,ds_y,teacher1_x,teacher1_y,teacher1_dist)):
            gg=True
        if (is_hit(ds_x,ds_y,teacher2_x,teacher2_y,teacher2_dist)):
            gg=True
    pygame.display.update()
#===主程式結束===#