from tkinter import Tk, ttk




class Board:
    def __init__(self):
        self.board = Tk()
        self.board.title("Tic Tac toe : Player 1")
        st = ttk.Style()
        st.configure("my.TButton", font=('Chiller', 24, 'bold'))

    def drawGridLines(self):
        b1 = ttk.Button(self.board, text=" ", style="my.TButton")
        b1.grid(row=1, column=0, sticky="snew", ipadx=50, ipady=50)

        b2 = ttk.Button(self.board, text=" ", style="my.TButton")
        b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)

        b3 = ttk.Button(self.board, text=" ", style="my.TButton")
        b3.grid(row=1, column=2, sticky="snew", ipadx=50, ipady=50)

        b4 = ttk.Button(self.board, text=" ", style="my.TButton")
        b4.grid(row=2, column=0, sticky="snew", ipadx=50,
                ipady=50)

        b5 = ttk.Button(self.board, text=" ", style="my.TButton")
        b5.grid(row=2, column=1, sticky="snew", ipadx=50, ipady=50)

        b6 = ttk.Button(self.board, text=" ", style="my.TButton")
        b6.grid(row=2, column=2, sticky="snew", ipadx=50,
                ipady=50)

        b7 = ttk.Button(self.board, text=" ", style="my.TButton")
        b7.grid(row=3, column=0, sticky="snew", ipadx=50,
                ipady=50)

        b8 = ttk.Button(self.board, text=" ", style="my.TButton")
        b8.grid(row=3, column=1, sticky="snew", ipadx=50,
                ipady=50)

        b9 = ttk.Button(self.board, text=" ", style="my.TButton")
        b9.grid(row=3, column=2, sticky="snew", ipadx=50,
                ipady=50)

        self.board.resizable(0, 0)
        self.board.mainloop()
