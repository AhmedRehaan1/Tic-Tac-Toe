class Menu:
    def __init__(self):
        self.items=[]
    def main_menu(self):
        print("Main Menu")
        print("1-start game")
        print("2-End game")
        choice = input("Enter your choice: as 1 or 2: ")
        if self.validate_choice(choice):
            return choice
        
    def end_menu(self):
        print("End Menu")
        print("1-Play again")
        print("2-Exit")
        choice = input("Enter your choice: as 1 or 2: ")
        if self.validate_choice(choice):
            return choice

    def validate_choice(self, choice):
        if choice in ['1', '2']:
            return True
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return False