from sprint3_0.product.board import Board


class GUI:
    global board

    def __init__(self):
        pass

    def drawEmptyBoard(self):
        global board
        board = Board()
        board.drawGridLines()

    def drawNonEmptyBoard(self):
        global board
        board = Board()
        board.drawGridLines(f1=True, f2=True, f3 =True, f4= True, f5=True, f6=True, f7=True, f8=True, f9=True)

    def drawXWon(self):
        global board
        board = Board()
        board.drawGridLines(f1=True, f5=True, f2=True, f4=True, f3=True)

    # # # acceptance criterion 4.2
    # # # @Test
    def drawOWon(self):
        global board
        board = Board()
        board.drawGridLines(f9=True, f1=True, f5=True, f2=True, f4=True, f3=True)

    #  acceptance criterion 4.3
    #  @Test
    def drawDraw(self):
        global board
        board = Board()
        board.drawGridLines(f2=True, f1=True, f3=True, f6=True, f4=True, f5=True, f9=True, f7=True, f8=True)



if __name__ == '__main__':
    g1 = GUI()
    g1.drawEmptyBoard()
    g1.drawNonEmptyBoard()
