from game import start_new_game, game_ended, display_board, play_again
from words.words import get_random_word
from difficulty_selector import set_difficulty
from language_selector import words
from guess import get_guess


def get_win_message():
    return f'You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)}, the word was "{secret_word}"'


def get_loss_message():
    return 'Yes! The secret word is "' + secret_word + '"! You have won!'


print('H A N G M A N')

set_difficulty()

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)

while True:
    print('The secret word is in the set: ' + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    # Let the player type in a letter.
    guess = get_guess(missed_letters + correct_letters)

    # Ask the player if they want to play again (but only if the game is done).
    if game_ended(guess, get_win_message(), get_loss_message(), missed_letters, correct_letters, secret_word):
        if play_again():
            start_new_game(missed_letters, correct_letters, secret_word, secret_set)
        else:
            break