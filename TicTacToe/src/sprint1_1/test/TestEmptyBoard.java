package sprint1_1.test;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import sprint1_1.product.Board;

public class TestEmptyBoard {

	private Board board = new Board();

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	// acceptance criterion 1.1
	@Test
	public void testNewBoard() {
		for (int row = 0; row<3; row++) {
			for (int column = 0; column<3; column++) {
				assertEquals("", board.getCell(row, column), 0); 
			}
		}
		assertEquals("", board.getTurn(), 'X'); 
	}
	
	// acceptance criterion 1.2
	@Test
	public void testInvalidRow() {
		assertEquals("", board.getCell(3, 0), -1); 
	}

	// acceptance criterion 1.3
	@Test
	public void testInvalidColumn() {
		assertEquals("", board.getCell(0, 3), -1); 
	}
}
