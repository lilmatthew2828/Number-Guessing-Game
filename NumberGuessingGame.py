'''
Matthew Kilpatrick
5/2/24
Mini Project 1
Number Guessing Game
'''

import numpy
import pandas
import random
import pygame
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import deque
import tkinter as tk
import math

print("Welcome to my number guessing game")
'''
Steps into building the program are as follows: 
    Build a Number guessing game, in which the user selects a range.
    Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
    Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
'''
class NumberGuessingGame:
    def __init__(self):
        self.name = str(input("Enter your name: "))
        self.minimum = int(input("Enter a minimum range for the random number: "))
        self.maximum = int(input("Enter a maximum range for the random number: "))
        self.random_number = random.randint(self.minimum,self.maximum)
    def start_the_guessing_game(self):
        print(f"\n{self.name.upper()} Now we will start the guessing game!!!\n"
              f"\tRemeber that the number you are trying to guess is between {self.minimum} and {self.maximum}")
        guess = int(input("Enter your guess here, you get 5 guesses: "))
        if (guess > self.random_number):
            print("To high!!!")
        elif (guess < self.random_number):
            print("To low!!!")
        number_of_guess = 0
        num_of_guess_left = 5
        correct = False
        while guess != self.random_number and number_of_guess != 5:
            guess = int(input(f"Wrong Luh Nigga, Try again, {num_of_guess_left-1} guess left: "))
            if (guess > self.random_number):
                print("To high!!!")
            elif (guess < self.random_number):
                print("To low!!!")
            number_of_guess += 1
            num_of_guess_left -= 1
        print(f"The Random Number that was generated: {self.random_number}")





