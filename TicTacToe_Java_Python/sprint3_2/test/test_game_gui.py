import time
import unittest

from sprint3_2.product.tictoctoe_gui import TicTocToeGUI


class TestGameGUI(unittest.TestCase):
    global game

    # @before
    def setUp(self):
        pass

    # @after
    def tearDown(self):
        pass

    def testEmptyBoard(self):
        global game
        game = TicTocToeGUI()
        game.drawEmptyTicTocToeGUI()


    def testNonEmptyBoard(self):
        global game
        game = TicTocToeGUI()
        game.drawNonEmptyTicTocToeGUI()



if __name__ == '__main__':
    unittest.main()

