from player import player_lost
from guess import evaluate_guess
from pictures import HANGMAN_PICS
from language_selector import words
from words.words import get_random_word


def start_new_game(missed_letters, correct_letters, secret_word, secret_set):
    missed_letters = ''
    correct_letters = ''
    secret_word, secret_set = get_random_word(words)


def game_ended(guess, win_message, loss_message, missed_letters, correct_letters, secret_word):
    """"Returns True if the game ended, False otherwise
    
        The game ends when:
            * evaluate_guess() returns True -> the player won
            * player_lost() returns True

        Parameters:
            Are used only if the game ends

            win_message : str
                Printed if the game ended because the user won
            
            loss_message : str
                Printed if the game ended because the user lost
    """

    if evaluate_guess(guess, missed_letters, correct_letters, secret_word):
        print(win_message)
    elif player_lost(missed_letters): # if evaluation returns false, we need to know why 
        # the board is displayed one last time
        display_board(missed_letters, correct_letters, secret_word)
        print(loss_message)
    else:
        return False
    return True

from pictures import HANGMAN_PICS


def display_board(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def play_again():
    """returns True if the player wants to play again, otherwise it returns False"""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')