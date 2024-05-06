import random

class Sudoku:
    def __init__(self):
        self.original_board = [[0 for i in range(9)] for j in range(9)]
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.remove_cell = [[0 for i in range(9)] for j in range(9)]
        self.board_offset()

    def board_offset(self):
        seq = [i for i in range(1, 10)]
        diag = [i for i in range(0, 10, 3)]

        for k in range(3):
            random.shuffle(seq)
            index = 0
            for i in range(diag[k], diag[k + 1]):
                for j in range(diag[k], diag[k + 1]):
                    self.original_board[i][j] = seq[index]
                    index += 1

    def generate_board(self):
        flag = False
        while not flag:
            count = 0
            while count < 9 * 9:

                i, j = count // 9, count % 9

                if self.original_board[i][j] != 0:
                    count += 1
                else:
                    seq = [i for i in range(1, 10)]
                    random.shuffle(seq)

                    for k in range(9):
                        self.original_board[i][j] = seq[k]
                        row = 0
                        col = 0
                        sqr = 0
                        for n in range(9):
                            if self.original_board[i][n] == seq[k]:
                                row += 1
                            if self.original_board[n][j] == seq[k]:
                                col += 1
                            if self.original_board[i - (i % 3) + (n // 3)][j - (j % 3) + (n % 3)] == seq[k]:
                                sqr += 1
                        if row == 1 and col == 1 and sqr == 1:
                            count += 1
                            break

            for n in range(1, 10):
                count = 0
                for i in range(9):
                    for j in range(9):
                        if self.original_board[i][j] == k:
                            count += 1
                if count != 9:
                    flag = False
                    break
            flag = True

        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.original_board[i][j]
        return True

    def clear(self):
        self.original_board = [[0 for i in range(9)] for j in range(9)]
        self.board = [[0 for i in range(9)] for j in range(9)]

    def generate_sudoku(self):
        self.clear()
        self.generate_board()
        return self.board

    def generate_puzzle(self):
        self.board = self.generate_sudoku()
        remove_count = 0

        while remove_count < 60:
            i, j = random.randint(0, 8), random.randint(0, 8)
            if self.board[i][j] == 0:
                continue
            else:
                self.remove_cell[i][j] = self.board[i][j]
                self.board[i][j] = 0
                remove_count += 1

        return self.board

    def check_answer(self, puzzle):
        count = 0
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != self.original_board[i][j]:
                    count += 1
        if count:
            return False
        else:
            return True


        



