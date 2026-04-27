# Mathias Bernat - CMPSC 132 Final 'Tic-Tac-Toe'

PROJECT DESCRIPTION

This project is a terminal-based 2-player Tic-tac-toe game. User input is used to make moves on the game board, which is
displayed in the terminal. The objective is to align 3 consecuative symbols in a row, column or diagonal before your 
opponent can. The game can be replayed until the user wishes for the program to end.

The core of the program is the 'Game' class, which contains attributes board and player (current player), and features
methods:
  play: controls game loop and validates user input
  print_board: displays game board
  move: updates game board after user input is validated
  check_win: checks board for all winning conditions
  check_draw: checks if board is full after all winning conditions are ruled out
  reset: clears game board and sets the player to 'X'

INSTRUCTIONS

1. Clone project files
2. Open Terminal
3. Navigate to directory and enter command: python final_project.py
4. Follow internal instructions when entering input
