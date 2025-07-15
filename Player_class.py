class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    def set_name(self):
        while True:
            name = input("Enter player name: ")
            if name.isalpha() and len(name) > 0:
                self.name = name
                break
            else:
                print("Invalid name. Please enter a valid name consisting of letters only.")
    def set_symbol(self):
        while True:
            symbol = input(f"Hello {self.name} Enter your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.capitalize() # Ensure the symbol is capitalized a >> A , x >> X
                break
            else:
                print("Invalid symbol. Please enter a single letter as the symbol.")
    