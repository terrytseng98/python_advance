import pygame
import random
import sys
import os
os.chdir(sys.path[0])
def check_click(pos1,x_start,y_start,x_end,y_end):
    x_match=pos1[0]>x_start and pos1[0]<x_end
    y_match=pos1[1]>y_start and pos1[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False
WHITE=(255,255,255)
Black=(0,0,0)
red=(255,0,0)
pygame.init()
bg_img="背景.png"
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()
gopher=pygame.image.load('地鼠.png')
a=0
screen=pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption('曾宥誠')
sur=pygame.Surface([bg_x,bg_y])
pos6=[[610,500],[190,500],[400,500],[190,360],[610,360],[400,360]]
tick=0
max_tick=30
pos=pos6[0]
clock=pygame.time.Clock()
font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr,36)
title=font.render(str(a),True,red)
tit_w=title.get_width()
tit_h=title.get_height()
act=False
while True:
    clock.tick(30)
    sur.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(pygame.mouse.get_pos(),pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                a+=1
                title=font.render(str(a),True,red)
    if tick>max_tick:
        new_pos=random.randint(0,5)
        pos=pos6[new_pos]
        tick=0
    else:
        tick=tick+1

    sur.blit(gopher,(pos[0]-gopher.get_width()/2,pos[1]-gopher.get_height()))
    screen.blit(sur,(0,0))
    screen.blit(title,(0,0))
    pygame.display.flip()