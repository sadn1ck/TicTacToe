# from tkinter import font

import pygame


pygame.init()
screen = pygame.display.set_mode((450, 500))
font = pygame.font.Font('CaviarDreams.ttf', 32)
pygame.display.set_caption('TicTacToe')
text = font.render('by sadn1ck', True, (0, 0, 0), (255, 253, 208))
textRect = text.get_rect()
textRect.center = (350, 25)
# to fill the screen with a color, use screen.fill(R,G,B)

running = True
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
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        print(event)
    pygame.display.update()