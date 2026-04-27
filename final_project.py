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

        pass


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
    

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    

    def play(self):

        self.reset()

        pass


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()