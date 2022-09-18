#===載入套件開始
from time import time
import pygame 
import sys 
import os 
os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***


#===初始化設定開始===
LIMIT_LOW=140
LIMIT_HIGH=140
pygame.init()
timer=0
clock=pygame.time.Clock()
#***初始化設定結束***


#===載入圖片開始===
img=pygame.image.load("image/bg.png")
img_dinosaur=[
    pygame.image.load("image/小恐龍1.png"),
    pygame.image.load("image/小恐龍2.png")
]
img_cacti=pygame.image.load("image/cacti.png")
#***載入圖片結束***


#===遊戲視窗設定開始===
bg_x=img.get_width()
bg_y=img.get_height()
bg_size=(bg_x,bg_y)
roll_x=0

pygame.display.set_caption("Dinosaur")
screen=pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***


#===分數設定開始===

#***分數設定結束***


#===恐龍設定開始===
ds_x=50
ds_y=LIMIT_LOW
jumpState=False
jumpValue=0
def move_dinosaur(win,timer):
    global ds_x, ds_y,jumpState,jumpValue
    if jumpState:
        if ds_y>=LIMIT_LOW:
            jumpValue=-10
        if ds_y<=0:
            jumpValue=10
        ds_y+=jumpValue
        if ds_y>=LIMIT_LOW:
            jumpState=False
    win.blit(img_dinosaur[timer%len(img_dinosaur)],[ds_x,ds_y])
#***恐龍設定結束***


#===仙人掌設定開始===
cacti_w=img_cacti.get_width()
cacti_h=img_cacti.get_height()
cacti_x=bg_x-100
cacti_y=LIMIT_LOW
cacti_shift=10
def move_cacti(win):
    global cacti_x,cacti_y,cacti_shift
    cacti_x-=cacti_shift
    if cacti_x<0:
        cacti_x=bg_x-100
        cacti_y=LIMIT_LOW
    win.blit(img_cacti,[cacti_x,cacti_y])
#***仙人掌設定結束***


#***碰撞設定開始***

#***碰撞設定結束***


#===GameOver設定開始===

#***GameOver設定結束***


#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(20)
    timer+=1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP and ds_y==LIMIT_LOW:
                jumpState=True
    #===遊戲結束===       

    #===遊戲進行===        
    roll_x=(roll_x-10) % bg_x
    print(roll_x)
    print(roll_x-bg_x)
    screen.blit(img,[roll_x-bg_x,0])
    screen.blit(img,[roll_x,0])
    move_dinosaur(screen,timer)
    move_cacti(screen)
    #===更新角色狀態===
    pygame.display.update()
#===主程式結束===