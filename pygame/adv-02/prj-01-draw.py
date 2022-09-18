import pygame
import sys

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
beight=500


screen=pygame.display.set_mode((width, beight))
pygame.display.set_caption('Game')

bg=pygame.Surface((width, beight))
bg.fill(blue)

font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr, 24)
title=font.render('START', True, white)
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
                if act==False:
                    act=True
                    title=font.render('START', True, white)

    if (act==True):
        pygame.draw.rect(bg,green,[5,45,200,200],0)
        pygame.draw.ellipse(bg,brown,[80,105,40,20],0)
        pygame.draw.ellipse(bg,brown,[65,120,70,30],0)
        pygame.draw.ellipse(bg,brown,[50,140,100,30],0)
        pygame.draw.ellipse(bg,brown,[35,160,130,30],0)
        pygame.draw.polygon(bg,brown,[[100,91],[90,112],[108,108]],0)
        pygame.draw.circle(bg,black,(90,115),5,0)
        pygame.draw.circle(bg,black,(110,115),5,0)
        pygame.draw.arc(bg,black,[90,126,20,10], math.radians(180), math.radians(0), 2)
        pygame.draw.line(bg,brown,(70,145),(30,120),3)
        pygame.draw.line(bg,brown,(130,145),(170,120),3)
    else:
        screen.blit(title,(0,0))
      #  pygame.display.update()

      #  print(pygame.mouse.get_pos())
    pygame.display.update()