import pygame
from sudokuSolver import*
size = WIDTH, HEIGHT = 600, 900
WHITE = 255, 255, 255
BLACK = 0, 0, 0


class Board:

    def __init__(self, startingPosition):
        self.rows = 9
        self.columns = 9
        self.width = 540
        self.height = 540 
        self.selected = None
        self.boxes = [[Box(startingPosition[i][j], i, j) for j in range(self.columns)] for i in range(self.rows)]
        self.currentPosition = startingPosition
        

    def click(self,pos):
        if pos[0] < self.width and pos[1] < self.height:
            x = pos[0] // 60
            y = pos[1] // 60
            return (int(y),int(x))
        else:
            return None

    def draw(self,screen):
        screen.fill(WHITE)
        for i in range(0,600,60):
            if i%180==0: 
                w=3
            else:
                w=1
            pygame.draw.line(screen,BLACK,(i,0),(i,540),w)
            pygame.draw.line(screen,BLACK,(0,i),(540,i),w)
        for i in range(self.rows):
            for j in range(self.columns):
                self.boxes[i][j].draw(screen)
    
    def clear(self):
        row, col = self.selected
        if self.boxes[row][col].value == 0:
            self.boxes[row][col].setTmp(0)

    def select(self, row, column):
        for i in range(self.rows):
            for j in range(self.columns):
                self.boxes[i][j].selected = False
        self.boxes[row][column].selected = True
        self.selected = (row,column)

    def place(self, value):
        row, column = self.selected
        if self.boxes[row][column].value == 0:
            

            if isPossible(self.currentPosition,row,column,value): 
                self.boxes[row][column].setValue(value)
                self.update()
                if solver(self.currentPosition):
                    return True
            else:
                self.boxes[row][column].setValue(0)
                self.boxes[row][column].setTmp(0)
                self.update()
                return False

    def sketch(self, value):
        row, column = self.selected
        self.boxes[row][column].setTmp(value)

    def update(self):
        self.currentPosition = [[self.boxes[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boxes[i][j].value == 0:
                    return False
        return True

class Box:
    def __init__(self, value, row, column):
        self.width = 60
        self.height = 60
        self.value = value
        self.tmp = 0
        self.selected = False
        self.row = row
        self.column = column
    
    def setValue(self, value):
        self.value = value

    def setTmp(self, tmp):
        self.tmp = tmp
    
    
    def draw(self, screen):
        fnt = pygame.font.SysFont("comicsans", 60)

        if self.value==0 and self.tmp!=0:
            text = fnt.render(str(self.tmp), 1, (128,128,128))
            screen.blit(text,(self.column*60+5, self.row*60+5))
        elif self.value!=0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            screen.blit(text, (self.column*60+30-text.get_width()/2, self.row*60+30-text.get_height()/2))
        
        if self.selected:
            points1 = ((self.column*60,0),(self.column*60+60,0),(self.column*60+60,540),(self.column*60,540))
            points2 = ((0,self.row*60),(0,self.row*60+60),(540,self.row*60+60),(540,self.row*60))
            pygame.draw.lines(screen,(0,0,255),True,points1,width=3)
            pygame.draw.lines(screen,(0,0,255),True,points2,width=3)
            pygame.draw.rect(screen, (0,255,0),(self.column*60,self.row*60,60,60),3)