"""
implement hangman game
words_repo has a list of ~500 words in english. 
we use this words for this game
a player gets 5 life to guess the word
if the player guess correctly inside 5 tries you win
few words in words list has - or whitespace
this words are not picked as it is not a valid hangman word

TODO: ask how many letter word user wants to guess?
TODO: show the hangman
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
    no_of_tries = 6  # or maybe more?
    # pick a word from the words list to play
    word_to_play = select_word_for_hangman(words)
    # these chars are what will be required as input.
    # any other char entered is invalid
    required_chars = set(word_to_play)
    # keep a list of all characters A-Z to compare
    all_chars = set(string.ascii_uppercase)
    # add the entered chars in this set so we can keep a track of entered values
    used_chars = set()

    print(f"You have to guess a {len(word_to_play)} letter word")
    while len(required_chars) > 0 and no_of_tries > 0:
        # print(f"You have {no_of_tries} chances to guess the {len(word_to_play)} letter word")
        print(f"You have {no_of_tries} chances to guess the word")
        word_list = [letter if letter in used_chars else '_' for letter in word_to_play]
        # display all the guessed characters and remaining as __
        print(" ".join(word_list))

        user_letter = input("Guess a letter in the word : ").upper()
        # first check if it is not guessed already
        if user_letter in all_chars - used_chars:
            # now add to the used chars set - i.e next time we can check if already guessed and display message
            used_chars.add(user_letter)
            if user_letter in required_chars:
                # if entered char is in our word then remove from required chars set
                required_chars.remove(user_letter)
            else:
                # if not in required word - then no of tries decreses by 1
                no_of_tries = no_of_tries - 1
                print("Wrong guess .. you lose one chance")
        elif user_letter in used_chars:
            print("You already guessed that letter .. try again")
        else:
            # is user enters numeric or special chars
            # TODO: maybe take away one try?
            print("Invalid input .. try again")

    if no_of_tries == 0:
        print(f"You exhausted all tries .. the word was {word_to_play}")
    else:
        print(f"Congrats! you guessed {word_to_play} correctly")


if __name__ == "__main__":
    play_hangman()
