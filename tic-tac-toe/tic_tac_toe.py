import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def printBoard(self):
        for row in [self.board[i*3:((i+1)*3)] for i in range(3)]:
            print('|' + '|'.join(row) + '|')


    @staticmethod
    def print_board_nums():

        nums_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

        for row in nums_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def nums_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter): 
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        else:
            return False
         
    def winner(self, square, letter):

        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind +1 )*3]

        # All letter in row
        if all([spot == letter for spot in row]):
            return True
        
        # All Column values
        col_ind = square%3
        col = [ self.board[col_ind +i *3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # Diagonals [0,2,4,6,8]

        # left_right diagonal [0,4,8]
        # right_left diagonal [2,4,6]
        if square % 2 == 0: 
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
    

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    square = None
    
    flag = game.empty_squares()

    while flag:

        if letter == 'X':
            square = x_player.get_move(game)
            print('X - player move', square)
        elif letter == 'O':
            square = o_player.get_move(game)
            print('O - player move', square)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square} ")
                game.printBoard()
            if game.current_winner:
                if print_game:
                    print(f'\n {letter}\'s Player Won ')
                    return letter
            print('')

        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
        flag = game.empty_squares()

        print(f'flag: ---> {flag}')
        time.sleep(0.8)

    if print_game:
        print(f'It\'s Tie .. !')
    


x_player = HumanPlayer("X")
o_player = ComputerPlayer("O")
t = TicTacToe()

play(t,x_player,o_player, print_game=True)

