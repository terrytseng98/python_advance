import pygame
import random
import sys
import os
import time
os.chdir(sys.path[0])

from pygame.locals import*
def check_click(pos1,x_start,y_start,x_end,y_end):
    x_match=pos1[0]>x_start and pos1[0]<x_end
    y_match=pos1[1]>y_start and pos1[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,0,255)
brown=(60,40,20)
black=(0,0,0)

pygame.init()
bg_img="背景.png"
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()

score=0
screen=pygame.display.set_mode([bg_x, bg_y])

sur=pygame.Surface([bg_x,bg_y])
pos6=[[610,450],[190,450],[400,450],[190,310],[610,310],[400,310]]
tick=0
max_tick=20
pos=pos6[0]
clock=pygame.time.Clock()

pygame.mouse.set_visible(False)
mpos=pygame.mouse.get_pos()

times=0
times_max=20

typeface=pygame.font.get_default_font()
font=pygame.font.Font(typeface,36)
title=font.render(str(score),True,red)

end_font=pygame.font.Font(typeface,36)
end_sur=end_font.render(str(times),True,red)

ham1=pygame.image.load("Hammer1.png")
ham2=pygame.image.load("Hammer2.png")
gopher1=pygame.image.load('地鼠.png')
gopher2=pygame.image.load("地鼠被打.png")
pygame.mixer.music.load("hit.mp3") 

while True:
    clock.tick(27)
    hammer=ham2
    hit=gopher1
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            hammer=ham1
            if check_click(pygame.mouse.get_pos(),pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                score+=1
                title=font.render(str(score),True,red)
                hit=gopher2
                pygame.mixer.music.play()
        elif event.type==MOUSEMOTION:
            mpos=pygame.mouse.get_pos()

    if times > times_max:
        sur.fill((0,0,0))
        pygame.mouse.set_visible(True)
        end_sur=font.render("Your Score is:{}/{}".format(score,times_max),True,green)
        screen.blit(sur,(0,0))
        screen.blit(end_sur,(0,0))
        pygame.display.flip()
    else:
        if tick>max_tick:
            times+=1
            score_sur=font.render(str(score),True,red)
            end_sur=font.render(str(times),True,red)
            new_pos=random.randint(0,5)
            pos=pos6[new_pos]
            tick=0
        else:
            tick=tick+1

        sur.blit(bg, (0,0))
        sur.blit(hit, (pos[0]-hit.get_width()/2, pos[1]-hit.get_height()/2))
        sur.blit(hammer, (mpos[0]-hammer.get_width()/2, mpos[1]-hammer.get_height()/2))

        screen.blit(sur,(0,0))
        screen.blit(end_sur,(bg_x-end_sur.get_width()-10,10))    
        screen.blit(title,(0,0))
        pygame.display.flip()
        if (hammer==ham1):
            time.sleep(0.1)