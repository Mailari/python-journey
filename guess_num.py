import random

def guessX(x):
    ran_int =  random.randint(1,x)
    guess = 0

    while guess != ran_int:
        guess = int(input(f'Guess the number between 1 to {x}   : ---- '))
        if guess < ran_int: 
            print('Sorry, Guess Again!, Too low')
        elif guess > ran_int: 
            print('Sorry, Guess Again!, Too High')
    print(f"You guessed it right !!!")

def guessC(x):
    low = 0
    high = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too High(h), too Low(l), or Correct (c)")
        if feedback == 'l':
            low = guess
        elif feedback == 'h':
            high = guess
    print("I guessed it right!!")


game_type = input("----: Here we are at Guess number Game: --- \nIf you want to play(me) ! \nIf you want computer to guess(cu) ! \n")

if game_type == 'me':
    guessX(int(input("Guess Game Counter: --- ")))
elif game_type == 'cu':
    guessC(int(input("Guess Game Counter: --- ")))
else:
    print("Wrong Guess")