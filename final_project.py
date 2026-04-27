"""
Mathias Bernat
CMPSC 132 Final: 'Tic-Tac-Toe'
"""


class Game:

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player = 'X'


    def reset(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player = 'X'


    def print_board(self):
        for row in self.board:
            print('|'.join(row))


    def move(self,row,col):
        self.board[row][col] = self.player


    def check_win(self):
        board = self.board
        for i in range(3):
            if self.player == board[i][0] == board[i][1] == board[i][2]:
                return True
            if self.player == board[0][i] == board[1][i] == board[2][i]:
                return True
        
        if self.player == board[0][0] == board[1][1] == board[2][2]:
            return True
        if self.player == board[0][2] == board[1][1] == board[2][0]:
            return True
        
        return False
    

    def check_draw(self): # Only happens after board is checked for wins
        for row in self.board:
            if ' ' in row:
                return False
        return True
    

    def play(self):

        playing = True

        while playing:
            
            self.reset()
            game_over = False

            while not game_over:
                self.print_board()
            
                # Loop ensures valid input
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input(f'{self.player} player, enter your row (1-3): ')) - 1
                        col = int(input('Now enter your column (1-3): ')) - 1

                        valid_move = True

                        if row not in range(3) or col not in range(3):
                            print('Row or column out of range. Try again')
                            valid_move = False
                    
                        elif self.board[row][col] != ' ':
                            print('Spot taken. Select an open spot.')
                            valid_move = False

                
                    except ValueError:
                        print('Invalid input. Please enter an integer.')
            
                self.move(row,col)

                if self.check_win():
                    self.print_board()
                    print(f'{self.player} player wins!')
                    game_over = True
                elif self.check_draw():
                    self.print_board()
                    print('Draw.')
                    game_over = True
                else:
                    if self.player == 'X':
                        self.player = 'O'
                    else:
                        self.player = 'X'

            play_again = input('Would you like to play again? (Say "Yes" if so) ')
            if play_again != 'Yes':
                playing = False


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()