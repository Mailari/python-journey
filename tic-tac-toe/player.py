import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move():
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\s turn. Input move(0 to 8)')
            try:
                val = int(square)
                if val not  in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Please Enter Valid Input")
        return val