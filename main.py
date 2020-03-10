import pygame

pygame.init()
screen = pygame.display.set_mode((450, 500))
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
coord = {0: (75, 125),
         1: (225, 125),
         2: (375, 125),
         3: (75, 275),
         4: (225, 275),
         5: (375, 275),
         6: (75, 425),
         7: (225, 425),
         8: (375, 425)}


# function to display cross and circle according to click coordinates and chance
def display_sign(ind, sign):
    if index != -1:
        if sign == 0:
            screen.blit(circle, coord[ind])
        if sign == 1:
            screen.blit(cross, coord[ind])


running = True
who = 0 # check if player will draw cross or circle

while running:
    screen.fill((255, 253, 208))

    pygame.draw.line(screen, (255, 255, 255), (0, 50), (500, 50))
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (500, 200))
    pygame.draw.line(screen, (0, 0, 0), (0, 350), (500, 350))
    pygame.draw.line(screen, (0, 0, 0), (0, 500), (500, 500))

    pygame.draw.line(screen, (0, 0, 0), (150, 50), (150, 500))
    pygame.draw.line(screen, (0, 0, 0), (300, 50), (300, 500))
    pygame.draw.line(screen, (0, 0, 0), (450, 50), (450, 500))
    # pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            click_coord = event.pos
            click_x = click_coord[0]
            click_y = click_coord[1]
            index = getIndex(click_x, click_y)
            display_sign(index, who)

    pygame.display.update()
