import unittest

from sprint3_0.product.gui import GUI


class TestBoardGUI(unittest.TestCase):
    global board

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmptyBoard(self):
        global board
        board = GUI()
        board.drawEmptyBoard()

    def testNonEmptyBoard(self):
        global board
        board = GUI()
        board.drawNonEmptyBoard()


if __name__ == "__main__":
    unittest.main()
