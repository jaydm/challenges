#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters():
    chosen = []
    chosen_letters = []

    while len(chosen) < NUM_LETTERS:
        choice = random.randrange(0, len(POUCH))

        if (choice not in chosen):
            chosen.append(choice)
            chosen_letters.append(POUCH[choice])

    return chosen_letters

def get_possible_dict_words(selection):
    possible = []

    for word in DICTIONARY:
        letters = list(word.upper())

        used = []

        for letter in selection:
            if letter in letters:
                used.append(letter)
                letters.remove(letter)

        if len(letters) == 0:
            possible.append(word)

    return possible

def _get_permutations_draw(draw):
    return itertools.permutations(draw) 

def _validation(test, letters):
    for word in get_possible_dict_words(letters):
        if word.upper() == test:
            return True

    return False

def main():
    drawn_letters = draw_letters()
    user_word = '~'

    while not _validation(user_word, drawn_letters):
        print(drawn_letters)
        user_word = input('Enter a word using these letters: ').upper()

    word_value = calc_word_value(user_word)

    print(f'The value of your word is: {word_value}')
    
    possible_words = get_possible_dict_words(drawn_letters)

    max_word = max_word_value(possible_words)
    max_value = calc_word_value(max_word)

    print(f'The possible word with the highest score is: {max_word} with a value of {max_value}')

    ratio = (calc_word_value(user_word) / calc_word_value(max_word))

    print(f'Your score is: {ratio}')

    pass

if __name__ == "__main__":
    main()
