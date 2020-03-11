import pygame
import sys
from main2 import PvC
from main import PvP
pygame.init()
HEIGHT = 500
WIDTH = 450
COL1 = (255, 253, 208)
COL2 = (255, 0, 0)
choice = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('img/gameicon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('TicTacToe')
font = pygame.font.Font('CaviarDreams.ttf', 32)
pvptext = font.render('Player vs Player', True, COL1, COL2)
pvp_rect=pvptext.get_rect()
pvp_rect.center = (225, 127)
pvctext = font.render('Player vs Computer', True, COL1, COL2)
pvc_rect=pvptext.get_rect()
pvc_rect.center = (200, 310)
screen_open = True
fontSmall = pygame.font.Font('CaviarDreams.ttf', 16)
aboutus = fontSmall.render('By Arnab Sen and Anik Das, students of IIEST, Shibpur',True, (0, 0, 0), COL1)
about_rect=aboutus.get_rect()
about_rect.center = (227, 425)
aboutarnab = fontSmall.render('https://github.com/mr-daredevil',True, (0, 0, 0), COL1)
aboutanik = fontSmall.render('https://github.com/sadn1ck',True, (0, 0, 0), COL1)

about_rectarnab=aboutarnab.get_rect()
about_rectarnab.center = (220, 455)

about_rectanik=aboutanik.get_rect()
about_rectanik.center = (222, 475)

while screen_open:
    
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                click_coord = event.pos
                click_x = click_coord[0]
                click_y = click_coord[1]
                if(click_x < 400 and click_x >50):
                    if(click_y<180 and click_y>80):
                        PvP()
                    elif (click_y<360 and click_y>260):
                        PvC()
    choice.fill(COL1)
    pygame.draw.rect(choice, COL2, (50, 80, 350, 100))
    pygame.draw.rect(choice, COL2, (50, 260, 350, 100))
    choice.blit(pvptext, pvp_rect)
    choice.blit(pvctext, pvc_rect)
    choice.blit(aboutus, about_rect)
    choice.blit(aboutarnab, about_rectarnab)
    choice.blit(aboutanik, about_rectanik)
    pygame.display.flip()
    pygame.display.update()
            
