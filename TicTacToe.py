import pygame, sys
import numpy as np



pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
Rows = 3
Columns = 3
Circle_radius = 60
Circle_width = 15
Cross_width = 25
Space = 55

RED = (255, 0, 0)
Circle_Color = (239, 231, 200)
Cross_Color = (66, 66, 66)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption( 'Tic Tac Toe' )
screen.fill(BG_COLOR)

board = np.zeros( (Rows, Columns) )


def draw_line():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(Rows):
        for col in range(Columns):
            if board[row][col] == 1 :
                pygame.draw.circle(screen, Circle_Color, (int( col * 200 + 100), int(row * 200 + 100)), Circle_radius, Circle_width)
            elif board[row][col] == 2 :
                pygame.draw.line(screen, Cross_Color, (col * 200 + Space, row * 200 + 200 - Space), (col * 200 + 200 - Space, row * 200 + Space ), Cross_width)
                pygame.draw.line(screen, Cross_Color, (col * 200 + Space, row * 200 + Space), (col * 200 + 200 - Space, row * 200 + 200 - Space ), Cross_width)

def game(row, col, player):
    board[row][col] = player


def available (row, col):
    return board[row][col] == 0

def board_full ():
    for row in range(Rows):
      for col in range(Columns):
            if board[Rows][Columns] == 0:
                return False
    return True
def check_win(player):
    for row in range(Rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player : #for horizontal
            draw_horizontal_winning_line(row, player)
            return True

    for col in range(Columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player : #for vertical
           draw_vertical_winning_line(col, player)
           return True

    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        draw_cross2_winning_line(player)
        return True
    elif (board[2][0] == player and board[1][1] == player and board[0][2] == player):
        draw_cross1_winning_line(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_cross1_winning_line(player):
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = Cross_Color
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_cross2_winning_line(player):
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = Cross_Color

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)



draw_line()
player = 1
game_over = False

def restart():
    screen.fill(BG_COLOR)
    draw_line()
    for row in range(Rows):
        for col in range (Columns):
            board[row][col] = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if (available( clicked_row, clicked_col)):
                if player == 1:
                    game(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    game(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player = 1
                game_over = False
                restart()

    pygame.display.update()

