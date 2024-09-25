import random
from utilities.hangman_words import words
import string

def get_verified_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return str(word).upper()

def hangman():
    word = get_verified_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 10
    
    while len(word_letter) > 0 and lives > 0 :

        if used_letters :
            print("\nYou used these letter, ", ' '.join(used_letters))
            print("Lives: ---> ", lives)
        
        current_word = [letter if letter in used_letters else '-' for letter in word ]
        print("Current Word: ", ' '.join(current_word))

        user_letter = input("Guess Letter: ---->").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                lives = lives + 1
                word_letter.remove(user_letter)
        elif user_letter in used_letters:
            print("You already used the Letter :--- ", user_letter)
        else:
            print("Invalid Character")

        lives = lives - 1

        if lives == 0:
            print("You lost, Unable to guess the Word:---> ", ' '.join(word_letter))        
            break
    if lives > 0:
        print("\n You Guessed it right...!  \t  The Word: ", word.upper())
    else:
        print("\n You are out of guesses ..! The word is ", word)

hangman()