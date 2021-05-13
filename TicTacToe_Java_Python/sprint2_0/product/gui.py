from sprint2_0.product.board import Board


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
        board.drawGridLines(f1=True, f5=True)



if __name__ == '__main__':
    g1 = GUI()
    g1.drawEmptyBoard()
    g1.drawNonEmptyBoard()
