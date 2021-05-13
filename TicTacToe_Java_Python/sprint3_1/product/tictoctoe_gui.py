from sprint3_1.product.tictoctoe_game import TicTocToeGame


class TicTocToeGUI:
    global board

    def __init__(self):
        pass

    def drawEmptyTicTocToeGUI(self):
        global board
        board = TicTocToeGame()
        board.drawGridLines()

    def drawNonEmptyTicTocToeGUI(self):
        global board
        board = TicTocToeGame()
        board.drawGridLines(f1=True, f5=True)

    def drawXWon(self):
        global board
        board = TicTocToeGame()
        board.drawGridLines(f1=True, f5=True, f2=True, f4=True, f3=True)

    # # # acceptance criterion 4.2
    # # # @Test
    def drawOWon(self):
        global board
        board = TicTocToeGame()
        board.drawGridLines(f9=True, f1=True, f5=True, f2=True, f4=True, f3=True)

    #  acceptance criterion 4.3
    #  @Test
    def drawDraw(self):
        global board
        board = TicTocToeGame()
        board.drawGridLines(f2=True, f1=True, f3=True, f6=True, f4=True, f5=True, f9=True, f7=True, f8=True)



if __name__ == '__main__':
    g1 = TicTocToeGUI()
    g1.drawEmptyTicTocToeGUI()
    g1.drawNonEmptyTicTocToeGUI()
