import random

def play():
    print("---- : Let Play Rock,Paper,Scissors : ------")
    player = input("'r' for Rock, 'p' for Paper, 's' Scissors \n")

    if player not in ['r', 'p', 's']:
        print('Invalid Input')
        return

    computer = random.choice(['r','p','s'])
    print(f"Yours :--- {player} and Computer's : ---- {computer}")

    if player == computer:
        print("It\'s Tie ...!")
    
    elif is_win(player,computer):
        print("You won ...!")
    else:
        print("You lost ...!")



def is_win(p, c):
    # return True if win
    # conditions r > s, s > p , p > r 
    return (p == 'r' and c == 's') or (p == 's' and c == 'p') or (p == 'p' and c == 'r')
        
    
     
play()