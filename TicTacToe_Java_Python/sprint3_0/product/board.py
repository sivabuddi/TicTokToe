from tkinter import Tk, ttk,Button
from tkinter import messagebox
import random



activePlayer = 1
p1 = []
p2 = []
mov = 0

b1 = ''
b2 = ''
b3 = ''
b4 = ''
b5 = ''
b6 = ''
b7 = ''
b8 = ''
b9 = ''


class Board():

    def __init__(self):
        self.board = Tk()
        self.board.title("Tic Tac toe : Player 1")
        st = ttk.Style()
        st.configure("my.TButton", font=('Chiller', 24, 'bold'))

    def checkWinner(self):
        winner = -1
        if (1 in p1) and (2 in p1) and (3 in p1):
            winner = 1
        if (1 in p2) and (2 in p2) and (3 in p2):
            winner = 2

        if (4 in p1) and (5 in p1) and (6 in p1):
            winner = 1
        if (4 in p2) and (5 in p2) and (6 in p2):
            winner = 2

        if (7 in p1) and (8 in p1) and (9 in p1):
            winner = 1
        if (7 in p2) and (8 in p2) and (9 in p2):
            winner = 2

        if (1 in p1) and (4 in p1) and (7 in p1):
            winner = 1
        if (1 in p2) and (4 in p2) and (7 in p2):
            winner = 2

        if (2 in p1) and (5 in p1) and (8 in p1):
            winner = 1
        if (2 in p2) and (5 in p2) and (8 in p2):
            winner = 2

        if (3 in p1) and (6 in p1) and (9 in p1):
            winner = 1
        if (3 in p2) and (6 in p2) and (9 in p2):
            winner = 2

        if (1 in p1) and (5 in p1) and (9 in p1):
            winner = 1
        if (1 in p2) and (5 in p2) and (9 in p2):
            winner = 2

        if (3 in p1) and (5 in p1) and (7 in p1):
            winner = 1
        if (3 in p2) and (5 in p2) and (7 in p2):
            winner = 2

        if winner == 1:
            messagebox.showinfo(title="Congratulations.",
                                message="Player 1 (X) is the winner")
        elif winner == 2:
            messagebox.showinfo(title="Congratulations.",
                                message="Player 2 (O) is the winner")
        elif mov == 9:
            messagebox.showinfo(title="Draw",
                                message="It's a Draw!!")

    def setLayout(self, id, player_symbol):
        if id == 1:
            b1.config(text=player_symbol)
            b1.state(['disabled'])
        elif id == 2:
            b2.config(text=player_symbol)
            b2.state(['disabled'])
        elif id == 3:
            b3.config(text=player_symbol)
            b3.state(['disabled'])
        elif id == 4:
            b4.config(text=player_symbol)
            b4.state(['disabled'])
        elif id == 5:
            b5.config(text=player_symbol)
            b5.state(['disabled'])
        elif id == 6:
            b6.config(text=player_symbol)
            b6.state(['disabled'])
        elif id == 7:
            b7.config(text=player_symbol)
            b7.state(['disabled'])
        elif id == 8:
            b8.config(text=player_symbol)
            b8.state(['disabled'])
        elif id == 9:
            b9.config(text=player_symbol)
            b9.state(['disabled'])

    def buttonClick(self, id):

        global activePlayer
        global p1, p2
        global mov

        if (activePlayer == 1):
            self.setLayout(id, "X")
            p1.append(id)
            mov += 1
            self.board.title("Tic Tac Toe : Player 2")
            activePlayer = 2

        elif (activePlayer == 2):
            self.setLayout(id, "O")
            p2.append(id)
            mov += 1
            self.board.title("Tic Tac Toe : Player 1")
            activePlayer = 1

        self.checkWinner()


    def enableAll(self):
        b1.config(text=" ")
        b1.state(['!disabled'])
        b2.config(text=" ")
        b2.state(['!disabled'])
        b3.config(text=" ")
        b3.state(['!disabled'])
        b4.config(text=" ")
        b4.state(['!disabled'])
        b5.config(text=" ")
        b5.state(['!disabled'])
        b6.config(text=" ")
        b6.state(['!disabled'])
        b7.config(text=" ")
        b7.state(['!disabled'])
        b8.config(text=" ")
        b8.state(['!disabled'])
        b9.config(text=" ")
        b9.state(['!disabled'])

    def restart(self):
        global p1, p2, mov, activePlayer
        p1.clear();
        p2.clear()
        mov, ActivePlayer = 0, 1
        self.board.title("Tic Tac Toe : Player 1")
        self.enableAll()

    def drawGridLines(self, f1=False, f2=False, f3=False, f4=False, f5=False, f6=False, f7=False, f8=False, f9=False):
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        b1 = ttk.Button(self.board, text=" ", style="my.TButton")
        b1.grid(row=1, column=0, sticky="snew", ipadx=50, ipady=50)
        if f1 == True:
            b1.config(command=lambda: self.buttonClick(1))

        b2 = ttk.Button(self.board, text=" ", style="my.TButton")
        b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
        if f2 == True:
            b2.config(command=lambda: self.buttonClick(2))

        b3 = ttk.Button(self.board, text=" ", style="my.TButton")
        b3.grid(row=1, column=2, sticky="snew", ipadx=50, ipady=50)
        if f3 == True:
            b3.config(command=lambda: self.buttonClick(3))

        b4 = ttk.Button(self.board, text=" ", style="my.TButton")
        b4.grid(row=2, column=0, sticky="snew", ipadx=50, ipady=50)
        if f4 == True:
            b4.config(command=lambda: self.buttonClick(4))

        b5 = ttk.Button(self.board, text=" ", style="my.TButton")
        b5.grid(row=2, column=1, sticky="snew", ipadx=50, ipady=50)
        if f5 == True:
            b5.config(command=lambda: self.buttonClick(5))

        b6 = ttk.Button(self.board, text=" ", style="my.TButton")
        b6.grid(row=2, column=2, sticky="snew", ipadx=50, ipady=50)
        if f6 == True:
            b6.config(command=lambda: self.buttonClick(6))

        b7 = ttk.Button(self.board, text=" ", style="my.TButton")
        b7.grid(row=3, column=0, sticky="snew", ipadx=50, ipady=50)
        if f7 == True:
            b7.config(command=lambda: self.buttonClick(7))

        b8 = ttk.Button(self.board, text=" ", style="my.TButton")
        b8.grid(row=3, column=1, sticky="snew", ipadx=50, ipady=50)
        if f8==True:
            b8.config(command=lambda: self.buttonClick(8))

        b9 = ttk.Button(self.board, text=" ", style="my.TButton")
        b9.grid(row=3, column=2, sticky="snew", ipadx=50, ipady=50)
        if f9==True:
            b9.config(command=lambda: self.buttonClick(9))

        Button(text="New Game..", font=('ubuntu', 28, 'bold'), bg='green', fg='white', border=5, width=8, command=lambda: self.restart()).grid(row=0, column=1, sticky="we")
        #Button(text="New Game..", font=('ubuntu', 28, 'bold'), bg='red', fg='white', border=5, width=4,command=lambda: self.Restart()).grid(row=0, column=1, sticky="we")
        self.board.resizable(0,0)
        self.board.mainloop()


# if __name__ == '__main__':
#     board = Board()
#     board.drawGridLines(f1=True,f2=True,f3=True,f4=True,f5=True,f6=True,f7=True,f8=True,f9=True)