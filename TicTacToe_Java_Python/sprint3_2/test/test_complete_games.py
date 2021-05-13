import unittest

from sprint3_2.product.tictoctoe_gui import TicTocToeGUI


class TestCompleteGames(unittest.TestCase):
    global game

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # acceptance criterion 4.1
    # @Test
    def testXWon(self):
        global game
        game = TicTocToeGUI()
        game.drawXWon()

    # # # acceptance criterion 4.2
    # # # @Test
    def testOWon(self):
        global game
        game = TicTocToeGUI()
        game.drawOWon()

    #  acceptance criterion 4.3
    #  @Test
    def testDraw(self):
        global game
        game = TicTocToeGUI()
        game.drawDraw()


if __name__ == '__main__':
    unittest.main()
