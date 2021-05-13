from sprint1_1.product.board import Board


class GUI:
    global board

    def __init__(self):
        pass

    def drawEmptyBoard(self):
        global board
        board = Board()
        board.drawGridLines()


if __name__ == '__main__':
    GUI().drawEmptyBoard()
