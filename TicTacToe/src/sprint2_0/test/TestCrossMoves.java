package sprint2_0.test;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import sprint2_0.product.Board;

public class TestCrossMoves {

	private Board board;

	@Before
	public void setUp() throws Exception {
		board = new Board();
	}

	@After
	public void tearDown() throws Exception {
	}

	// acceptance criterion 2.1
	@Test
	public void testCrossTurnMoveVacantCell() {
		board.makeMove(0, 0);
		assertEquals("", board.getCell(0, 0), 1);
		assertEquals("", board.getTurn(), 'O');
	}

	// acceptance criterion 2.2
	@Test
	public void testCrossTurnMoveNonVacantCell() {
		board.makeMove(0, 0);
		board.makeMove(1, 0);
		assertEquals("", board.getCell(1, 0), 2);
		assertEquals("", board.getTurn(), 'X');
		board.makeMove(0, 0);
		assertEquals("", board.getTurn(), 'X');
	}

	// acceptance criterion 2.3 - 1
	@Test
	public void testCrossTurnInvalidRowMove() {
		board.makeMove(4, 0);
		assertEquals("", board.getTurn(), 'X');
	}

	// acceptance criterion 2.3 - 2
	@Test
	public void testCrossTurnInvalidColumnMove() {
		board.makeMove(0, 4);
		assertEquals("", board.getTurn(), 'X');
	}

}
