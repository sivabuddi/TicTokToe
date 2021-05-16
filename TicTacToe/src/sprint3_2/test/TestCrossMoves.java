package sprint3_2.test;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import sprint3_2.product.TicTacToeGame;
import sprint3_2.product.TicTacToeGame.Cell;

public class TestCrossMoves {

	private TicTacToeGame game;

	@Before
	public void setUp() throws Exception {
		game = new TicTacToeGame();
	}

	@After
	public void tearDown() throws Exception {
	}

	// acceptance criterion 2.1
	@Test
	public void testCrossTurnMoveVacantCell() {
		game.makeMove(0, 0);
		assertEquals("", game.getCell(0, 0), Cell.CROSS);
		assertEquals("", game.getTurn(), 'O');
	}

	// acceptance criterion 2.2
	@Test
	public void testCrossTurnMoveNonVacantCell() {
		game.makeMove(0, 0);
		game.makeMove(1, 0);
		assertEquals("", game.getCell(1, 0), Cell.NOUGHT);
		assertEquals("", game.getTurn(), 'X');
		game.makeMove(0, 0);
		assertEquals("", game.getTurn(), 'X');
	}

	// acceptance criterion 2.3
	@Test
	public void testCrossTurnInvalidRowMove() {
		game.makeMove(4, 0);
		assertEquals("", game.getTurn(), 'X');
	}

	// acceptance criterion 2.3
	@Test
	public void testCrossTurnInvalidColumnMove() {
		game.makeMove(0, 4);
		assertEquals("", game.getTurn(), 'X');
	}

}
