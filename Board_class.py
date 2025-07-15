class Board:
    def __init__(self):
        self.board=[]
        for i in range(1,10):
            self.board.append(str(i))  # Initialize board with string representations of numbers 0-9
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)
    def update_board(self, position, player_symbol):
        while True:
            if self.board[position] not in ['X', 'O']:
                self.board[position] = player_symbol
                return True
        else:
            print("Position already taken. Choose another position.")
            return False

    def reset_board(self):
        for i in range(9):
            if self.board[i] in ['X', 'O']:
                self.board[i] = str(i)