import random


class GameBoard:

    def __init__(self, board_size, number_bombs):
        self.board_size = board_size
        self.number_bombs = number_bombs
        self.uncovered_places = set()
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.user_board = [['?' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.place_bombs()
        self.calculate_neighbors_bombs()

    def place_bombs(self):
        bombs_placed = 0
        while bombs_placed < self.number_bombs:
            place = random.randint(0, self.board_size ** 2 - 1)
            r = place // self.board_size
            c = place % self.board_size
            if self.board[r][c] == '*':
                continue
            self.board[r][c] = '*'
            bombs_placed += 1

    def calculate_neighbors_bombs(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] == '*':
                    continue
                for row in range(max(0, r - 1), min(r + 2, self.board_size)):
                    for col in range(max(0, c - 1), min(c + 2, self.board_size)):
                        if self.board[row][col] == '*':
                            self.board[r][c] += 1

    def uncover_place(self, row, col):
        self.uncovered_places.add((row, col))
        if self.board[row][col] == '*':
            self.user_board[row][col] = '*'
            return True
        elif self.board[row][col] > 0:
            self.user_board[row][col] = self.board[row][col]
            return False
        else:
            self.user_board[row][col] = 0
            for n_row in range(max(0, row - 1), min(row + 2, self.board_size)):
                for n_col in range(max(0, col - 1), min(col + 2, self.board_size)):
                    if (n_row, n_col) in self.uncovered_places:
                        continue
                    self.uncover_place(n_row, n_col)
            return False

    def print_user_board(self):
        string_to_print = '    '
        for i in range(self.board_size):
            string_to_print += str(i + 1) + ' '
        string_to_print += '\n----'
        for i in range(self.board_size - 1):
            string_to_print += '--'
        string_to_print += '-\n'
        for r in range(self.board_size):
            string_to_print += str(r + 1) + ' | '
            for c in range(self.board_size):
                string_to_print += str(self.user_board[r][c]) + ' '
            string_to_print += '\n'
        print(string_to_print)
        print('\n')

    def print_result_board(self):
        string_to_print = '    '
        for i in range(self.board_size):
            string_to_print += str(i + 1) + ' '
        string_to_print += '\n----'
        for i in range(self.board_size - 1):
            string_to_print += '--'
        string_to_print += '-\n'
        for r in range(self.board_size):
            string_to_print += str(r + 1) + ' | '
            for c in range(self.board_size):
                string_to_print += str(self.board[r][c]) + ' '
            string_to_print += '\n'
        print(string_to_print)
        print('\n')


while 1:
    my_board_size = input('How big shall the side of the board be? Type a positive integer   ')
    try:
        my_board_size = int(my_board_size)
        if my_board_size > 0:
            break
        else:
            print('Invalid number for the size of the board, try again')
    except:
        print('Invalid number for the size of the board, try again')

while 1:
    number_of_bombs = input('How many bombs? Type a positive integer   ')
    try:
        number_of_bombs = int(number_of_bombs)
        if number_of_bombs > 0:
            break
        else:
            print('Invalid number for the number of bombs, try again')
    except:
        print('Invalid number for the number of bombs, try again')

my_board = GameBoard(my_board_size, number_of_bombs)
game_over = False
my_board.print_user_board()
while not game_over:
    while 1:
        user_choice = input('Select your square of choice (Example: "1,2")   ')
        user_choice = user_choice.split(',')
        try:
            row_choice = int(user_choice[0]) - 1
            col_choice = int(user_choice[1]) - 1
            if row_choice < 0 or col_choice < 0 or col_choice > my_board.board_size or row_choice > my_board.board_size:
                print('Invalid choice, try again')
            else:
                break
        except:
            print('Invalid choice, try again')
    game_over = my_board.uncover_place(row_choice, col_choice)
    my_board.print_user_board()
    if len(my_board.uncovered_places) == my_board.board_size ** 2 - my_board.number_bombs:
        my_board.print_result_board()
        print('You won!')
        break
if game_over:
    print('You lost :(')
