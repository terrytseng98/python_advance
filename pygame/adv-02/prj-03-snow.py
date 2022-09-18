import pygame
import random
def check_click(pos,x_start,y_start,x_end,y_end):
    x_match=pos[0]>x_start and pos[0]<x_end
    y_match=pos[1]>y_start and pos[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False
WHITE=(255,255,255)
Black=(0,0,0)
pygame.init()
bg_x=640
bg_y=400
screen=pygame.display.set_mode((bg_x,bg_y))
pygame.display.set_caption('曾宥誠')
bg_img="pygame/adv-02/snow.jpg"
bg=pygame.image.load(bg_img)
font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr,36)
title=font.render('Start',True,Black)
tit_w=title.get_width()
tit_h=title.get_height()
act=False
x_site=random.randrange(0,bg_x)
y_site=random.randrange(0,bg_y)
x_shift=random.randint(-1,1)
radius=random.randint(4,6)
clock=pygame.time.Clock()
while True:
    clock.tick(20)
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(pygame.mouse.get_pos(),0,0,tit_w,tit_h):
                if act==False:
                    act=True
                    title=font.render('Start',True,Black)
                elif act==True:
                    act=False
                    title=font.render('Stop',True,Black)
    pygame.draw.circle(screen,WHITE,(x_site,y_site),radius-3)
    x_site+=x_shift
    y_site+=radius
    if y_site>bg_y:
        y_site=random.randrange(-10,-1)
        x_sute=random.randrange(0,bg_x)
    screen.blit(title,(0,0))
    pygame.display.update()













