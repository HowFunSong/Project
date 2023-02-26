from turtle import Screen, width
import numpy as np
from numpy.lib.function_base import blackman
import pygame
import sys
import math



BLUE = (0,50,150)
Black = (0,0,0)
RED = (255,50,0)
YELLOW = (255,200,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():                #做出指定大小的棋盤
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board,row,col,piece): #當放球時從def get_next_open_row中取得row的位置。
    board[row][col] = piece           #將矩陣中的對應row/col設置成1(放置狀態)

#檢查放球的位置是否是一個有效的位置
def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board,col):    #判斷要放置球的column中，最上面沒放球的位置
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))    #旋轉棋盤 根據(board,"旋轉軸")

def winning_move(board,piece):
    #check horizontal location for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece :
                return True
    #check vertical location for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece :
                return True    
    #check positive slope 
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece :
                return True       

    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece :
                return True      


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,(r+1)*SQUARESIZE,SQUARESIZE,SQUARESIZE))               #移動球
            pygame.draw.circle(screen,Black,(int((c+0.5)*SQUARESIZE),int((r+1.5)*SQUARESIZE)),RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1 :    
                pygame.draw.circle(screen,RED,(int((c+0.5)*SQUARESIZE),heigth - int((r+0.5)*SQUARESIZE)),RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen,YELLOW,(int((c+0.5)*SQUARESIZE),heigth - int((r+0.5)*SQUARESIZE)),RADIUS)
    pygame.display.update()


board = create_board()   #用矩陣先做出6*7 的棋盤    
print_board(board)
game_over = False        #設置bool值讓遊戲判斷是否繼續
turn = 0                 #turn 判斷現在是哪個玩家的遊戲回合


pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
heigth = (ROW_COUNT+1) * SQUARESIZE

size = (width,heigth)

RADIUS = int(SQUARESIZE/2-5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace",70,"Calibri")



while not game_over :

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,Black,(0,0,width,SQUARESIZE))
    
            posx = event.pos[0]
            if turn == 0 :
                pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
            elif turn == 1 :
                pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)),RADIUS)
        pygame.display.update()
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            pygame.draw.rect(screen,Black,(0,0,width,SQUARESIZE))
    #Ask for player 1 input
            if turn == 0:

                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                if winning_move(board,1):
                    lable = myfont.render("Player 1 Wins",1,RED,)
                    screen.blit(lable,(40,10))
                    
                    
                    print("PLAYER 1 Wins!!! Congrats!!!")
                    game_over = True
                
                
                
            # #Ask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))                
            
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                if winning_move(board,2):
                    lable = myfont.render("Player 2 Wins!",1,YELLOW)
                    screen.blit(lable,(40,10))
                    print("PLAYER 2 Wins!!! Congrats!!!")
                    game_over = True
                    
                
            turn += 1
            turn = turn % 2
            print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(2000)



