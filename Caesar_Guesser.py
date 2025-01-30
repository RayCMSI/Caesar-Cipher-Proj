# The guessing game of cracking the code by the user

from Caesar_Cipher import * 
from Phrases import * 
import random

class Caesar_Guess():

    def __init__(self) -> None:
        pass
    
    def run_game(self):
        guesses = 3
        secret_phrase = random.choice(Phrase().get_phrases())

        cipher = Cipher().caesar_encoder(secret_phrase, random.randint(1,26))

        print('This is the ciphered phrase: ', cipher)

        while guesses > 0:
            self.guess = input('Please Enter Your Geuss or Type "Hint" for a hint: ')

            if self.guess == 'Hint':
                print('A word in the phrase is: ', Phrase().get_hint(secret_phrase))

            if self.guess == secret_phrase:
                print(f'You guessed the correct phrase: {secret_phrase}')
                return
            elif self.guess != secret_phrase and self.guess != "Hint":
                print('You guessed the wrong phrase')
            
            guesses -= 1
        print('The correct phrase was:', secret_phrase)


if __name__ == '__main__':
    cg = Caesar_Guess()
    cg.run_game()