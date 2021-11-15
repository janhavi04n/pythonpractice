"""
implement hangman game
words_repo has a list of 500 words in english. we use this words for this game
a player gets 5 life to guess the word
if the player guess inside 5 tries you win
few words in words list has - or whitespace
this words are not picked as it is not a valid hangman word
"""
import random
import string
from words_repo import words


def select_word_for_hangman(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    return word.upper()


def play_hangman():
    no_of_tries = 5  # or maybe more?
    # pick a word from the words list to play
    word_to_play = select_word_for_hangman(words)
    # these chars are what will be required as input.
    # any other char entered is invalid
    required_chars = set(word_to_play)
    # keep a list of all characters A-Z to compare
    all_chars = set(string.ascii_uppercase)
    used_chars = set()




if __name__ == '__main__':
    play_hangman()
