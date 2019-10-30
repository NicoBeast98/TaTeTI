class TaTeTi():
    def __init__(self, board=None):
        if board is None:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = board

    def full(self):
        full = True
        for value in self.board:
            if value == ' ':
                full = False
        return full

    def win(self):
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[1] != ' ':
                return True
        if self.board[3] == self.board[4] == self.board[5]:
            if self.board[4] != ' ':
                return True
        if self.board[6] == self.board[7] == self.board[8]:
            if self.board[7] != ' ':
                return True
        if self.board[0] == self.board[3] == self.board[6]:
            if self.board[3] != ' ':
                return True
        if self.board[1] == self.board[4] == self.board[7]:
            if self.board[4] != ' ':
                return True
        if self.board[2] == self.board[5] == self.board[8]:
            if self.board[5] != ' ':
                return True
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board[4] != ' ':
                return True
        if self.board[2] == self.board[4] == self.board[6]:
            if self.board[4] != ' ':
                return True
        return False

    def validate(self, pos):
        if self.board[pos - 1] == ' ':
            return True
        else:
            return False

    def assign(self, pos, piece):
        if not (self.validate(pos)):
            raise Exception
        else:
            self.board[pos - 1] = piece

    def draw_board(self):
        display = "\n"
        for n in range(9):
            if self.board[n] != " ":
                display += " " + self.board[n] + " "
            else:
                display += " " + str(1+n) + " "
            if n == 2 or n == 5:
                display += "\n---+---+---\n"
            elif n == 8:
                display += "\n"
            else:
                display += "|"
        return display
