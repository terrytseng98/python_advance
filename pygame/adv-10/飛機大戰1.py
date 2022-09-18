#===載入套件開始===
import pygame
import sys
import os
os.chdir(sys.path[0])
from pygame.locals import *
import random
#***載入套件結束***

#===初始化設定開始===
pygame.init()
clock = pygame.time.Clock()
timer = 0
MISSILE_MAX=200
#***初始化設定結束***

#===載入圖片開始===
'''載入背景圖片'''
img_bg = pygame.image.load("image/space.png")
'''載入飛船圖片'''
img_sship = [
    pygame.image.load("image/fighter_M.png"),
    pygame.image.load("image/fighter_L.png"),
    pygame.image.load("image/fighter_R.png"),
]
'''載入飛船火焰'''
img_burn = pygame.image.load("image/starship_burner.png")
img_weapon = pygame.image.load("image/bullet.png")
img_enemy = pygame.image.load("image/enemy1.png")
#***載入圖片結束***
#===遊戲視窗設定開始===
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
pygame.mixer.music.load("image/airplane_notice.mp3")
pygame.mixer.music.play()


#***遊戲視窗設定結束***

#===捲動背景設定開始===
roll_y=0
roll_x=0
def roll_bg(win):
    global roll_y ,roll_x
    if key[pygame.K_DOWN]:
        roll_y = (roll_y - 2) % bg_y
        win.blit(img_bg, [0, roll_y - bg_y])
        win.blit(img_bg, [0, roll_y])
    if key[pygame.K_UP]:
        roll_y = (roll_y + 2) % bg_y
        win.blit(img_bg, [0, roll_y - bg_y])
        win.blit(img_bg, [0, roll_y])
    roll_y = (roll_y + 1) % bg_y
    win.blit(img_bg, [0, roll_y - bg_y])
    win.blit(img_bg, [0, roll_y])
#===捲動背景設定結束===

#===我機設定開始===
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
burn_w, burn_h = img_burn.get_rect().size
ss_sur = img_sship[0]
def move_starship(win, key, timer):
    global ss_x, ss_y, ss_sur
    ss_sur = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 20
        if ss_y < ss_hh:
            ss_y = ss_hh
    if key[pygame.K_DOWN]:
        ss_y += 20
        if ss_y > bg_y - ss_hh:
            ss_y = bg_y - ss_hh
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_sur = img_sship[1]
        if ss_x < ss_wh:
            ss_x = ss_wh
    if key[pygame.K_RIGHT]:
        ss_x += 20
        ss_sur = img_sship[2]
        if ss_x > bg_x - ss_wh:
            ss_x = bg_x - ss_wh
    win.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + (timer % 3) * 2])
    win.blit(ss_sur, [ss_x - ss_wh, ss_y - ss_hh])
#***我機設定結束***

#===飛彈設定開始===
msl_no=0
msl_f=[False]*MISSILE_MAX
msl_x=[0]*MISSILE_MAX
msl_y=[0]*MISSILE_MAX
msl_wh=img_weapon.get_width()/2
msl_hh=img_weapon.get_height()/2
msl_shift=50

def move_missile(win,key):
    global msl_f,msl_y,msl_x,msl_no

    if key[K_SPACE]:
        if timer%5==0:
            if msl_f[msl_no]==False:
                msl_f[msl_no]=True
                msl_x[msl_no]=ss_x-msl_wh 
                msl_y[msl_no]=ss_y-msl_hh
                msl_no+=1
                msl_no%=MISSILE_MAX
                pygame.mixer.music.load("image/槍聲.mp3")
                pygame.mixer.music.play()
    for i in range(MISSILE_MAX):
        if msl_f[i]==True:
            msl_y[i]=msl_y[i]-msl_shift
            win.blit(img_weapon,[msl_x[i],msl_y[i]-msl_hh])
            if msl_y[i]<0:
                msl_f[i]=False
#***飛彈設定結束***

#===敵機設定開始===
emy_f=False
emy_x=0
emy_y=bg_y+10
emy_wh=img_enemy.get_width()/2
emy_hh=img_enemy.get_height()/2
emy_shift=5

def move_enemy(win):
    global emy_f,emy_y,emy_x

    if emy_y>bg_y:
        emy_f=True
        emy_x=random.randint(emy_wh,bg_x-emy_wh)
        emy_y=random.randint(emy_hh,emy_hh+100)

    if emy_f==True:
        emy_y=emy_y+emy_shift
        win.blit(img_enemy,[emy_x,emy_y])
        if emy_y<0:
            emy_f=False
#***敵機設定結束***

#===碰撞偵測設定開始===
#***碰撞偵測設定結束***

#===爆炸設定開始===
#***爆炸設定結束***

#===保護罩設定開始===
#***保護罩設定結束***

#===主程式開始===
while True:
    clock.tick(30)
    key = pygame.key.get_pressed()
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)
    roll_bg(screen)
    move_starship(screen,key,timer)
    move_missile(screen,key)
    move_enemy(screen)
    pygame.display.update()
#===主程式結束===