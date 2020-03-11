import pygame
import sys
import time

pygame.init()
HEIGHT = 500
WIDTH = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('CaviarDreams.ttf', 32)
pygame.display.set_caption('TicTacToe')
cross = pygame.image.load('img/cross.png')
circle = pygame.image.load('img/circle.png')


def getIndex(x, y):
    if 0 < x < 149:
        if 50 < y < 199:
            return 0
        if 201 < y < 349:
            return 3
        if 351 < y < 500:
            return 6
        else:
            return -1
    elif 151 < x < 299:
        if 50 < y < 199:
            return 1
        if 201 < y < 349:
            return 4
        if 351 < y < 500:
            return 7
        else:
            return -1
    elif 301 < x < 450:
        if 50 < y < 199:
            return 2
        if 201 < y < 349:
            return 5
        if 351 < y < 500:
            return 8
        else:
            return -1
    else:
        return -1


board = [-1] * 9  # initialising the board with -1, which means no moves

# dictionary of index and render coordinate
coord ={0: (50, 100),
        1: (200, 100),
        2: (350, 100),
        3: (50, 250),
        4: (200, 250),
        5: (350, 250),
        6: (50, 400),
        7: (200, 400),
        8: (350, 400)}

# function to display cross and circle according to click coordinates and chance
def display_sign(ind, sign):
    if ind != -1:
        if sign == 0:
            screen.blit(circle, coord[ind])
        if sign == 1:
            screen.blit(cross, coord[ind])


running = True
who = 1 # check if player will draw cross or circle
moves = 0 #total number of moves so far

def display_board():
    for val in range(9):
        if board[val] == 1:
            display_sign(val, 1)
        elif board[val] == 0:
            display_sign(val, 0)

def check_game_over(moves):
    if moves < 5:
        return False
    elif board[0]==board[1]==board[2] and board[0]!=-1:
        return True 
    elif board[3]==board[4]==board[5] and board[3]!=-1:
        return True
    elif board[6]==board[7]==board[8] and board[6]!=-1:
        return True
    elif board[0]==board[3]==board[6] and board[0]!=-1:
        return True 
    elif board[1]==board[4]==board[7] and board[1]!=-1:
        return True
    elif board[2]==board[5]==board[8] and board[6]!=-1:
        return True
    elif board[0]==board[4]==board[8] and board[0]!=-1:
        return True 
    elif board[2]==board[4]==board[6] and board[2]!=-1:
        return True
    else:
        return False

while running:
    screen.fill((255, 253, 208))
    if(moves == 9):
        print("Draw!")
        running = False
        pygame.quit()
        sys.exit()
        quit()
    if(check_game_over(moves)):
        if who == 0:
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")
        running = False
        pygame.quit()
        sys.exit()
        quit()
    pygame.draw.line(screen, (255, 255, 255), (0, 50), (500, 50))
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (500, 200))
    pygame.draw.line(screen, (0, 0, 0), (0, 350), (500, 350))
    pygame.draw.line(screen, (0, 0, 0), (0, 500), (500, 500))

    pygame.draw.line(screen, (0, 0, 0), (150, 50), (150, 500))
    pygame.draw.line(screen, (0, 0, 0), (300, 50), (300, 500))
    pygame.draw.line(screen, (0, 0, 0), (450, 50), (450, 500))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            click_coord = event.pos
            click_x = click_coord[0]
            click_y = click_coord[1]
            index = getIndex(click_x, click_y)
            if(board[index]==-1):               
                board[index]=who
                moves += 1
                if who == 0: 
                    who = 1
                else:
                    who = 0
    display_board()
    pygame.display.flip()
    pygame.display.update()
