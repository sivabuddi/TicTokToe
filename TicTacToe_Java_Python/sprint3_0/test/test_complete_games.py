import unittest

from sprint3_0.product.gui import GUI


class TestCompleteGames(unittest.TestCase):
    global board

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # acceptance criterion 4.1
    # @Test
    def testXWon(self):
        global board
        board = GUI()
        board.drawXWon()


    # # # acceptance criterion 4.2
    # # # @Test
    def testOWon(self):
        global board
        board = GUI()
        board.drawOWon()

    #  acceptance criterion 4.3
    #  @Test
    def testDraw(self):
        global board
        board = GUI()
        board.drawDraw()


if __name__ == '__main__':
    unittest.main()
