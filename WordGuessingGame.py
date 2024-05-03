import random
import math
'''
Matthew Kilpatrick
5/2/24
Word Guessing Mini Game
'''

class WordGuesser:
    def __init__(self):
        self.name = str(input("What your full name: "))
        self.words = ["Machew", "Raven", 'rainbow', 'computer', 'science', 'programming',
                      'python', 'mathematics', 'player', 'condition',
                      'reverse', 'water', 'board', 'geeks']
        self.random_word = None
        self.list_of_characters = []

    def generate_rand_word (self):
        self.random_word = random.choice(self.words)
        self.list_of_characters.extend(self.random_word)
        print(self.list_of_characters)

    def guess_Word(self):

        def num_of_char_correct(users_guess):
            num_correct = 0
            if (users_guess == self.random_word):
                print("OMG, 😁 YOU GOT IT RIGHT 🥹 ")
                print("I ❤️ LUCKI!!!\n")
            else:
                for chars in users_guess:
                    if chars in self.list_of_characters:
                        num_correct += 1
                print(f"\t℗ You got {num_correct} characters correct!!")
                num_correct = 0

        # def is_correct(users_guess): # this function will end the program if the user enters the correct guess
        #     correct = False
        #     if(users_guess == self.random_word):
        #         print("OMG, ☺︎YOU GOT IT RIGHT☺︎ ")
        #         print("LUCKI IS MY KING!!!\n")

        number_of_guesses = 0
        number_of_guesses_left = 12 # a total of 12 guesses
        print("The List Of Random Words: ")
        for words in self.words:
            print(f"\t{words}")
        guess = str(input("Guess your word: "))
        # is_correct(users_guess=guess)
        num_of_char_correct(users_guess=guess)
        number_of_guesses_left -= 1
        number_of_guesses += 1
        print(f"\t ☢ You have #{number_of_guesses_left} guesses left ☢")
        print("-----------------------------------------")
        while (number_of_guesses != 12 and guess != self.random_word):
            guess = str(input("Wrong, Guess your word again: "))
            # is_correct(users_guess=guess)
            num_of_char_correct(users_guess=guess)
            number_of_guesses_left -= 1
            number_of_guesses += 1
            print(f"You have #{number_of_guesses_left} guesses left")
            num_of_chars_correct = 0
        print(f"The word that was randomly selected: {self.random_word}")






