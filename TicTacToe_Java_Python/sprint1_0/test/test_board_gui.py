import unittest

from sprint1_0.product.gui import GUI


class TestBoardGUI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmptyBoard(self):
        GUI().drawEmptyBoard()


if __name__ == "__main__":
    unittest.main()
