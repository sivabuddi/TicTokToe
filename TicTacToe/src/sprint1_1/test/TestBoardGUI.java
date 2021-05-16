package sprint1_1.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import sprint1_1.product.Board;
import sprint1_1.product.GUI;

public class TestBoardGUI {
	private Board board;

	@Before
	public void setUp() throws Exception {
		board = new Board();
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testEmptyBoard() {
		new GUI(board);
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

}
