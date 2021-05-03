""" How an amateur like me does it"""


def empty_grid():
    print(9 * "-")
    for i in range(3):
        print("|" + ' ' * 7 + "|")
    print(9 * "-")


class Tictac:
    def __init__(self):
        self.symbs = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.board = [[self.symbs[6], self.symbs[3], self.symbs[0]],
                      [self.symbs[7], self.symbs[4], self.symbs[1]],
                      [self.symbs[8], self.symbs[5], self.symbs[2]]]
        self.x, self.o = 0, 0
        self.xc, self.oc = 0, 0
        self.k = 0
        self.cord_input = [1, 2, 3]
        self.act_count = 1

    def count(self):

        for i in self.symbs:
            if i == "X":
                self.xc += 1
            elif i == "O":
                self.oc += 1

    def draw(self):

        print(9 * "-")
        print(f"| {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} |")
        print(f"| {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} |")
        print(f"| {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} |")
        print(9 * "-")

    def grid_values(self):

        while True:
            action = input("Enter the coordinates: ").split()
            if action[0].isdecimal() and action[1].isdecimal:
                if int(action[0]) > 3 or int(action[1]) > 3:
                    print("Coordinates should be from 1 to 3!")
                elif self.board[int(action[0]) - 1][int(action[1]) - 1] in ("X", "O"):
                    print("This cell is occupied! Choose another one!")
                else:
                    if self.act_count % 2:
                        self.board[int(action[0]) - 1][int(action[1]) - 1] = "O"

                    else:
                        self.board[int(action[0]) - 1][int(action[1]) - 1] = "X"

                    self.act_count += 1
                    self.k += 1
                    self.draw()
                    self.game_states()
                    break
            else:
                print("You should enter numbers!")

    def wins_row(self):
        if self.board[0][2] == self.board[1][2] == self.board[2][2] == "X":
            self.x += 1
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == "X":
            self.x += 1
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == "X":
            self.x += 1

        if self.board[0][2] == self.board[1][2] == self.board[2][2] == "O":
            self.o += 1
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == "O":
            self.o += 1
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == "O":
            self.o += 1

        if self.x or self.o == 1:
            pass
        else:
            self.wins_cols()

    def wins_cols(self):

        if self.board[0][2] == self.board[0][1] == self.board[0][0] == "X":
            self.x += 1
        elif self.board[1][2] == self.board[1][1] == self.board[1][0] == "X":
            self.x += 1
        elif self.board[2][2] == self.board[2][1] == self.board[2][0] == "X":
            self.x += 1

        if self.board[0][2] == self.board[0][1] == self.board[0][0] == "O":
            self.o += 1
        elif self.board[1][2] == self.board[1][1] == self.board[1][0] == "O":
            self.o += 1
        elif self.board[2][2] == self.board[2][1] == self.board[2][0] == "O":
            self.o += 1

        if self.x or self.o == 1:
            pass
        else:
            self.wins_diags()

    def wins_diags(self):

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == "X":
            self.x = 1
        elif self.board[2][2] == self.board[1][1] == self.board[0][0] == "X":
            self.x = 1

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == "O":
            self.o = 1
        elif self.board[2][2] == self.board[1][1] == self.board[0][0] == "O":
            self.o = 1

    def game_states(self):

        self.wins_row()
        #print(self.board)
        if self.x and self.o == 1:
            print("Impossible")
        elif (self.xc - self.oc) >= 2 or (self.oc - self.xc) >= 2:
            print("Impossible")
        elif self.x == 1:
            print("X wins")
        elif self.o == 1:
            print("O wins")
        elif self.act_count == 10:
            if self.x == 0 and self.o == 0 and "_" not in self.board:
                print("Draw")
            else:
                print("Game not finished")
        else:
            self.grid_values()


empty_grid()
ttt = Tictac()
ttt.grid_values()
