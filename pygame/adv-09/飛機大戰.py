#===載入套件開始===
import pygame
import sys
import os
os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***
#===初始化設定開始===
pygame.init()
clock = pygame.time.Clock()
timer = 0
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
#***載入圖片結束***
#===遊戲視窗設定開始===
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***
#===捲動背景設定開始===
roll_y = 0
def roll_bg(win):
    global roll_y
    roll_y = (roll_y + 50) % bg_y
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
#***飛彈設定結束***

#===敵機設定開始===
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
    move_starship(screen, key, timer)
    pygame.display.update()
#===主程式結束===