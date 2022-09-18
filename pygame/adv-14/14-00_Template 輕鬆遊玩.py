#===載入套件開始===
from colorsys import rgb_to_hls
from xmlrpc.server import DocXMLRPCRequestHandler
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import*
import random
#***載入套件結束***


#===初始化設定開始===
def resetGame():
    global brick_num, bricks_list, dx, dy, act

    for bricks in bricks_list:
        r=random.randint(100,200)
        g=random.randint(100,200)
        b=random.randint(100,200)
        bricks[5]=(r,g,b)
        bricks[4]=True
    act=False
    brick_num=total_block
    dx=8
    dy=-8
'''顏色'''
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
'''初始'''
gg=False
pygame.init()
life=3
'''時脈'''
clock=pygame.time.Clock()
act=False
gameover=pygame.image.load("image/gameover.png")
#***初始化設定結束***


#===遊戲視窗設定開始===
bg_x=800
bg_y=600
bg_size=(bg_x,bg_y)
pygame.display.set_caption(u"打磚塊遊戲")
screen=pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***


#===磚塊設定開始===
total_block=99
bricks_list=[]
brick_num=0
brick_x=70
brick_y=60
brick_w=0
brick_h=0
brick_v=True
for i in range(0,total_block):
    if ((i%11)==0):
        brick_w=0
        brick_h+=18
    bricks_list.append(
        [brick_w+brick_x,brick_h+brick_y,58,16,brick_v,blue])
    brick_w+=60

def bricks_update(win):
    global brick_num, dy
    '''磚塊'''
    for brick in bricks_list:
        if (brick[4]==True):
            if (is_hit(ball_x,ball_y,brick)):
                dy=-dy
                brick_num-=1
                brick[4]=False
            block_rect=[brick[0],brick[1],brick[2],brick[3]]
            pygame.draw.rect(win,brick[5],block_rect)\

            
            

#===磚塊設定結束===


# ===顯示磚塊數量設定開始===
typeface=pygame.font.get_default_font()
number_font=pygame.font.Font(typeface,36)

def get_block_num(win):
    global brick_num

    sur=number_font.render(str(brick_num),True,red)
    win.blit(sur,[10,10])
#===顯示磚塊數量設定結束===


#===碰撞設定開始===
def is_hit(x,y,boxRect):
    xmatch=x>=boxRect[0] and x<=boxRect[0]+boxRect[2]
    ymatch=y>=boxRect[1] and y<=boxRect[1]+boxRect[3]
    if (xmatch and ymatch):
        return True
    return False
#===碰撞設結束===


#===初始遊戲設定開始===
#===初始遊戲設定結束===


#===底板設定開始===
paddle_x=0
paddle_y=(bg_y -24)

def paddle_update(win):
    global dy,dx
    paddly_rect=[paddle_x,paddle_y, 1000,10]

    pygame.draw.rect(win,red,paddly_rect)

    if (is_hit(ball_x,ball_y,paddly_rect)):
        dy=-dy
#===底板設定結束===


#===球設定開始===
ball_x=400
ball_y=300
ball_radius=8
ball_diameter=ball_radius*2
ball_color=white
dx=8
dy=-8


def ball_update(win):
    global ball_x,ball_y
    global dx,dy,act,gg,life
    if (act==False):
        ball_x=paddle_x+500
        ball_y=paddle_y-ball_radius
    else:
        ball_x+=dx
        ball_y+=dy
        '''判斷死亡'''
        if (ball_y>bg_y-ball_diameter):
            act=False
            gg=True
            life-=1
        if (ball_x>bg_x-ball_diameter or ball_x<ball_diameter):
            dx=-dx
        if (ball_y>bg_y-ball_diameter or ball_y<ball_diameter):
            dy=-dy
    pygame.draw.circle(win,ball_color,[ball_x,ball_y],ball_radius)
#===球設定結束===
resetGame()
if brick_num<0:
    resetGame()
#===初始遊戲設定開始===
#===初始遊戲設定結束===
def live_update(win):
    global life

    sur=number_font.render(str(life),True,blue)
    win.blit(sur,[750,10])

gg_w=gameover.get_width()
gg_h=gameover.get_height()

def game_over(win):
    win.blit(gameover,((bg_x-gg_h)/2,(bg_y-gg_h)/2))

#-------------------------------------------------------------------------    
# 主迴圈.
#-------------------------------------------------------------------------
while True:
    if (life<=0):
        sys.exit()
    for event in pygame.event.get():
        '''離開遊戲'''
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            paddle_x=pygame.mouse.get_pos()[0]-500
        if event.type==pygame.MOUSEBUTTONDOWN:
            if (act==False):
                act=True
        if event.type==KEYDOWN:
            if event.key==K_RETURN and gg==True:
                gg=False
                resetGame()
    '''清除畫面'''
    screen.fill(black)

    if gg==True:
        #===遊戲結束===#
        game_over(screen)
    else:
        '''更新磚塊'''
        bricks_update(screen)
        '''顯示磚塊數量'''
        get_block_num(screen)
        '''顯示板子'''
        paddle_update(screen)
        '''更新球'''
        ball_update(screen)
        live_update(screen)
    '''更新畫面'''
    pygame.display.update()
    clock.tick(60)