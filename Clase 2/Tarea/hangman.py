from pictures import HANGMAN_PICS
from language_selector import words
from difficulty_selector import set_difficulty
from hangman_functions import get_random_word, display_board, get_guess, play_again


def start_new_game():
    global missed_letters, correct_letters, secret_word, secret_set
    missed_letters = ''
    correct_letters = ''
    secret_word, secret_set = get_random_word(words)


def player_won():
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letters:
            return False
    return True


def player_lost():
    return len(missed_letters) == len(HANGMAN_PICS) - 1


def print_loss_results():
    # the board is displayed one last time
    display_board(missed_letters, correct_letters, secret_word)

    print('You have run out of guesses!\nAfter ' 
    + str(len(missed_letters)) 
    + ' missed guesses and ' 
    + str(len(correct_letters)) 
    + ' correct guesses, the word was "' 
    + secret_word + '"')


def print_win_results():
    print('Yes! The secret word is "' + secret_word + '"! You have won!')


def evaluate_guess():
    """"Returns True only if the player won the game, false otherwise
    
        Remember:
            The function returns False but doesn't specify if the player lost
            or was just another missed letter
    """
    global missed_letters, correct_letters

    if guess in secret_word:
        correct_letters += guess

        if player_won():
            return True
    else:
        missed_letters += guess
        return False


def game_ended():
    """"Returns True if the game ended, False otherwise
    
        The game ends when:
            * evaluate_guess() returns True -> the player won
            * player_lost() returns True
    """
    global missed_letters, correct_letters

    if evaluate_guess():
        print_win_results()
    elif player_lost(): # if evaluation returns false, we need to know why 
        print_loss_results()
    else:
        return False
    return True


print('H A N G M A N')

set_difficulty()

start_new_game()

while True:
    print('The secret word is in the set: ' + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    # Let the player type in a letter.
    guess = get_guess(missed_letters + correct_letters)

    # Ask the player if they want to play again (but only if the game is done).
    if game_ended():
        if play_again():
            start_new_game()
        else:
            break