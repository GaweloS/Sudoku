import pygame
import sys
from sudokuSolver import solver, isPossible
from board import *

pygame.font.init()

clock = pygame.time.Clock()
size = WIDTH, HEIGHT = 600, 900
WHITE = 255, 255, 255
BLACK = 0, 0, 0

a = ([4,2,3,0,0,0,0,0,5],
    [0,0,0,0,0,3,0,0,0],
    [9,0,1,2,0,4,6,0,3],
    [2,0,0,0,4,5,0,7,1],
    [0,0,0,7,2,0,0,0,9],
    [7,3,4,8,0,0,0,5,0],
    [0,4,0,1,6,2,5,9,8],
    [8,5,0,0,0,0,0,0,0],
    [1,0,0,5,0,8,7,6,0])


def main():
    screen = pygame.display.set_mode((540,540))
    pygame.display.set_caption("Sudoku")
    board = Board(a)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.boxes[i][j].tmp != 0:
                        if board.place(board.boxes[i][j].tmp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        board.draw(screen)
        pygame.display.update()
        clock.tick(30)
main()
pygame.quit()
quit()