def PvC():
    import pygame
    import sys
    import time
    from generate import compMove # to import the function from another file
    pygame.init()
    HEIGHT = 500
    WIDTH = 450
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font('CaviarDreams.ttf', 32)
    s1 = 'Player\'s Move'
    s2 = 'Player2\'s Move'
    text1 = font.render(s1, True, (0, 0, 0)) 
    text2 = font.render(s2, True, (0, 0, 0)) 
    draw_text = font.render('Draw Match!', True, (0, 0, 0)) 
    p1Win = font.render('Player Wins!', True, (0, 0, 0)) 
    p2Win = font.render('Computer Wins!', True, (0, 0, 0)) 
    draw_textRect = draw_text.get_rect()
    p1WinRect = p1Win.get_rect()
    p2WinRect = p2Win.get_rect()
    text1Rect = text1.get_rect() 
    text2Rect = text2.get_rect()
    text1Rect.center = (WIDTH // 2, 25) 
    text2Rect.center = (WIDTH // 2, 25)
    draw_textRect.center = (WIDTH // 2, HEIGHT//2)
    p1WinRect.center = (WIDTH // 2, HEIGHT//2)
    p2WinRect.center = (WIDTH // 2, HEIGHT//2)   
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
    def update_who(who):
        return (who+1)%2

    def display_board():
        screen.blit(text1, text1Rect)
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
            screen.blit(draw_text, draw_textRect)
            pygame.display.flip()
            pygame.display.update
            time.sleep(2)
            # print("Draw!")
            running = False
            return
        if(check_game_over(moves)):
            if who == 0:
                # print("Player 2 Wins!")
                moves=9
                screen.blit(p1Win, p1WinRect)
                pygame.display.flip()
                pygame.display.update
                time.sleep(2)
            else:
                # print("Player 1 Wins!")
                screen.blit(p2Win, p2WinRect)
                pygame.display.flip()
                pygame.display.update
                time.sleep(2)
            running = False
            return
        pygame.draw.line(screen, (255, 255, 255), (0, 50), (500, 50))
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (500, 200))
        pygame.draw.line(screen, (0, 0, 0), (0, 350), (500, 350))
        pygame.draw.line(screen, (0, 0, 0), (0, 500), (500, 500))

        pygame.draw.line(screen, (0, 0, 0), (150, 50), (150, 500))
        pygame.draw.line(screen, (0, 0, 0), (300, 50), (300, 500))
        pygame.draw.line(screen, (0, 0, 0), (450, 50), (450, 500))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                click_coord = event.pos
                click_x = click_coord[0]
                click_y = click_coord[1]
                index = getIndex(click_x, click_y)
                if(board[index]==-1):               
                    board[index]=who
                    moves += 1
                    who = update_who(who)
                
                if(moves<9):
                    new_index = compMove(moves, board)
                    # print(moves, '->', new_index)
                    board[new_index]=who
                    moves += 1
                    who = update_who(who)
        display_board()
        pygame.display.flip()
        pygame.display.update()
