#===載入套件開始===
from email.mime import image
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
red=(255,0,0)
pygame.mixer.init()
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
img_enemy = [pygame.image.load("image/enemy1.png"),
            pygame.image.load("image/enemy2.png"),
            pygame.image.load("image/enemy3.png")]
img_explode = [
        None,
        pygame.image.load("image/explosion1.png"),
        pygame.image.load("image/explosion2.png"),
        pygame.image.load("image/explosion3.png"),
        pygame.image.load("image/explosion4.png"),
        pygame.image.load("image/explosion5.png"),]
img_shield=pygame.image.load("image/shield.png")
img_gg = pygame.image.load("image/gameover.png")

#===分數設定開始===
score=0
typeface=pygame.font.get_default_font()
score_font=pygame.font.Font(typeface,36)

def get_score(win):
    global score

    score_sur=score_font.render(str(score),True,red)
    win.blit(score_sur,[10,10])
#***分數設定結束***

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
hit=0
act=1
def move_starship(win, key, timer, emy):
    global ss_x, ss_y, ss_sur, ss_shield, ss_muteki, act
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
    if ss_muteki>0:
        ss_muteki=ss_muteki-1
        if ss_muteki%2==0:
            win.blit(img_burn,[ss_x-burn_w/2,ss_y+burn_h+(timer%3)*2])
            win.blit(ss_sur, [ss_x - ss_wh, ss_y - ss_hh])
        return
    for i in range(ENEMY_MAX):
        if emy[i]["STATE"]==True:
            w=emy[i]["IMG"].get_width()
            h=emy[i]["IMG"].get_height()
            r=int((w+h)/2)
            if is_hit(emy[i]["X"],emy[i]["Y"],ss_x-ss_wh,ss_y-ss_hh, r):
                ss_shield=ss_shield-20
                if ss_shield<=0:
                    ss_shield=0
                    act=0
                if ss_muteki==0:
                    ss_muteki=20
        win.blit(img_burn,[ss_x-burn_w/2,ss_y+burn_h+(timer%3)*2])
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
                mysound=pygame.mixer.Sound("image/槍聲.mp3")
                mysound.set_volume(0.2)
                mysound.play()
    for i in range(MISSILE_MAX):
        if msl_f[i]==True:
            msl_y[i]=msl_y[i]-msl_shift
            win.blit(img_weapon,[msl_x[i],msl_y[i]-msl_hh])
            if msl_y[i]<0:
                msl_f[i]=False
#***飛彈設定結束***

#===敵機設定開始===
mysound=pygame.mixer.Sound("image/Mechanized endurance. Battlefield brilliance. - 2022 ASUS TUF Gaming F15.mp3")
mysound.set_volume(0.5)
mysound.play(1000)
ENEMY_MAX=6
emy_f=False
emy_x=0
emy_y=bg_y+10
emy_shift=3
emy=[]
emy_exp = 0
for i in range(ENEMY_MAX):
    emy.append({
        "IMG": img_enemy[i % len(img_enemy)],
        "STATE": emy_f,
        "x": emy_x,
        "Y": emy_y,
        "S": emy_shift,
        "EXP":emy_exp
    })

def move_enemy(win,emy):
    global score

    emy_wh=int(emy["IMG"].get_width()/2)
    emy_hh=int(emy["IMG"].get_height()/2)
    emy_dist=int(emy_wh+emy_hh)
    if timer % 60==0:
        if emy["Y"]>bg_y:
            emy["STATE"]=True
            emy["X"]=random.randint(int(emy_wh),int(bg_x-emy_wh))
            emy["Y"]=random.randint(int(emy_hh),int(emy_hh+100))

    if emy["STATE"]==True:
        emy["Y"]+=emy["S"]
        for n in range(MISSILE_MAX):
            if msl_f[n]==True and is_hit(emy["X"],emy["Y"],msl_x[n],msl_y[n],emy_dist):
                msl_f[n]=False
                emy["STATE"]=False
                emy["EXP"]=1
                score+=1
                mysound=pygame.mixer.Sound("image/bomb.mp3")
                mysound.set_volume(0.1)
                mysound.play()
        win.blit(emy["IMG"],[emy["X"]-emy_wh,emy["Y"]-emy_hh])
#***敵機設定結束***

#===碰撞偵測設定開始===
def is_hit(x1,y1,x2,y2,r):
    if ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))<(r*r):
        return True
    else:
        return False
#***碰撞偵測設定結束***


#===爆炸設定開始===
exp_w, exp_h = img_explode[1].get_rect().size
def draw_explode(win,emy):
    if emy["EXP"]>0:
        win.blit(img_explode[emy["EXP"]],[emy["X"]-exp_w/2,emy["Y"]-exp_h/2])
        emy["EXP"]+=1
        if emy["EXP"]==6:
            emy["Y"]=bg_y+10
            emy["EXP"]=0
#***爆炸設定結束***

#===保護罩設定開始===
ss_shield=100
ss_muteki=0
sd_muteki=0
sd_w=img_shield.get_width()
sd_h=img_shield.get_height()

def get_shield(win):
    win.blit(img_shield, [0, bg_y - 40])
    pygame.draw.rect(win,(1,1,1),[ss_shield*4,bg_y-40,(100-ss_shield)*4,sd_h])

#***保護罩設定結束***

#===gameover設定開始===
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()
def game_over(win):
    win.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))
#***gameover設定結束***

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
    if act==1:          
        roll_bg(screen)
        move_starship(screen,key,timer,emy)
        move_missile(screen,key)
        for i in range(ENEMY_MAX):
            move_enemy(screen, emy[i])
            draw_explode (screen, emy[i])

        get_shield(screen)
        get_score(screen)
    else:
        game_over(screen)
    pygame.display.update()
#===主程式結束===