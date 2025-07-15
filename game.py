from Menu_class import Menu
from Board_class import Board
from Player_class import Player
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Game:
    current_player_index = 0
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
    def start_game(self):
        choice=self.menu.main_menu()
        if choice == '1':
            self.setup_players()
            self.play_game()
        elif choice == '2':
            self.end_game()
    def setup_players(self):
        for numbers,player in enumerate((self.players)):
            print(f"Player {numbers + 1} setup:")
            player.set_name()
            player.set_symbol()
            print("-"*20)
            clear_screen()
    def play_game(self):
        while True:
            self.board.display_board()
            self.player_turn()

            # Check if the player who just played has won
            if self.check_winner(self.players[1 - self.current_player_index]):
                self.board.display_board()
                print(f"Congratulations {self.players[1 - self.current_player_index].name}! You won!")
                choice = self.menu.end_menu()
                if choice == '1':
                    self.restart_game()
                elif choice == '2':
                    self.end_game()
                    break

        # Check for draw
            elif self.board_full():
                self.board.display_board()
                print("It's a draw!")
                choice = self.menu.end_menu()
                if choice == '1':
                    self.restart_game()
                elif choice == '2':
                    self.end_game()
                    break

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combination in winning_combinations:
            if all(self.board.board[i] == player.symbol for i in combination):
                return True
        return False
    def board_full(self):
        return all(cell in ['X', 'O'] for cell in self.board.board[1:10])
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()
        
    def player_turn(self):
        player = self.players[self.current_player_index]

        while True:
            try:
                choice = int(input(f"{player.name}, enter a position (1-8): "))
                choice=choice-1
                if 0 <= choice <= 8 and self.board.update_board(choice, player.symbol):
                    break
                else:
                    print("Invalid choice or position already taken.")
            except ValueError:
                print("Please enter a valid number between 0 and 8.")

        self.switch_player()

    def switch_player(self):
        self.current_player_index= 1-self.current_player_index
    def end_game(self):
        print("Game ended.")
        
game1 = Game()
game1.start_game()