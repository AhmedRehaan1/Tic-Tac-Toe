# Tic Tac Toe Game

This is a simple command-line Tic Tac Toe game implemented in Python.

## Features

*   Two-player game
*   Customizable player names and symbols
*   Winning condition checks (rows, columns, diagonals)
*   Draw condition check
*   Option to play again after a game ends

## Project Structure

The project is organized into several Python files, each responsible for a specific part of the game:

*   `game.py`: The main game logic, handling game flow, player turns, and win/draw conditions.
*   `Player_class.py`: Defines the `Player` class, managing player names and symbols.
*   `Menu_class.py`: Defines the `Menu` class, handling main menu and end-game menu interactions.
*   `Board_class.py`: Defines the `Board` class, managing the game board's state and display.

## How to Run

1.  **Prerequisites**

    Make sure you have Python 3 installed on your system.

2.  **Clone the repository (or download the files)**

    If you have Git, you can clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    Otherwise, download all the `.py` files into a single directory.

3.  **Run the game**

    Open your terminal or command prompt, navigate to the directory where you saved the files, and run:

    ```bash
    python3 game.py
    ```

## How to Play

1.  When the game starts, you will be presented with a main menu. Choose to start the game.
2.  You will be prompted to enter names and single-letter symbols for Player 1 and Player 2.
3.  The game board will be displayed. Players will take turns entering a number (1-9) corresponding to the position on the board where they want to place their symbol.
4.  The game will check for a winner after each move or if the board is full (draw).
5.  After a game ends, you will have the option to play again or exit.

## Code Overview

### `game.py`

This file contains the `Game` class, which orchestrates the entire game. It initializes the `Board`, `Player`, and `Menu` objects, and manages the game loop, player turns, and win/draw checks.

### `Player_class.py`

The `Player` class handles player-specific information such as their name and the symbol they use on the board (e.g., 'X' or 'O'). It includes methods for setting and validating player input for names and symbols.

### `Menu_class.py`

The `Menu` class provides the interactive menus for the game, including the main menu (start/end game) and the end-game menu (play again/exit). It also includes input validation for menu choices.

### `Board_class.py`

The `Board` class manages the Tic Tac Toe game board. It is responsible for:

*   Initializing the board with numbers 1-9.
*   Displaying the current state of the board.
*   Updating the board with player moves.
*   Resetting the board for a new game.

## Contributing

Feel free to fork this repository and contribute to the project. You can improve existing features, add new ones, or fix bugs.

## License

This project is open source and available under the [MIT License](LICENSE)
