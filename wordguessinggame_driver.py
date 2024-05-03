import random
import WordGuessingGame
'''
Matthew Kilpatrick
5/2/24
Word Guessing Mini Game
Driver File!!!!!!
'''
if __name__ == '__main__':
    machew = WordGuessingGame.WordGuesser()
    machew.generate_rand_word()
    machew.guess_Word()