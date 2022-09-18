import pygame
import sys
import math

def check_click(pos,x_start,y_start,x_end,y_end):
    x_match=pos[0]>x_start and pos[1]<x_end
    y_match=pos[1]>y_start and pos[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,0,255)
brown=(60,40,20)
black=(0,0,0)

width=500
beight=400


screen=pygame.display.set_mode((width, beight))
pygame.display.set_caption('Game')

bg_img='pygame/adv-02/snow.jpg'
bg=pygame.image.load(bg_img)



font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr, 24)
title=font.render('START', True, white)
tit_w=title.get_width()
tit_h=title.get_height()

font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr, 24)
title=font.render('STOP', True, white)
tit_w=title.get_width()
tit_h=title.get_height()

act=False

while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            #if check_click(pygame.mouse.)
                if act==True:
                    act=False
                    title=font.render('STOP', True, white)
                elif act==False:
                    act=True
                    title=font.render('START', True, white)



    screen.blit(title,(0,0))
      #  pygame.display.update()

      #  print(pygame.mouse.get_pos())
    pygame.display.update()