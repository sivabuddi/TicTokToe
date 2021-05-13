from sprintX_autoplay.auto_tictactoe import AutoTicTocToe


class TicTocToeGUI():

    def __init__(self):
        game = AutoTicTocToe()
        game.drawGridLines(f1=True, f2=True, f3=True, f4=True, f5=True, f6=True, f7=True, f8=True, f9=True)


if __name__ == '__main__':
    TicTocToeGUI()

