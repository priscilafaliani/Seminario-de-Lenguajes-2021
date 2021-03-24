from hangman_functions import get_random_word, display_board, get_guess, play_again
from language_selector import words
from pictures import HANGMAN_PICS


def set_medium_difficulty():
    """"Deletes the 2 levels of the game."""
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]


def set_hard_difficulty():
    """"Deletes 4 leves of the game."""
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]


def set_difficulty():
    """Prompts the user until a valid difficulty is entered and then sets it."""
    difficulty = 'X'
    while difficulty not in 'EMH':
        print('Enter difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()

    if difficulty == 'M':
        set_medium_difficulty()
    if difficulty == 'H':
        set_hard_difficulty()


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
    print('You have run out of guesses!\nAfter ' 
    + str(len(missed_letters)) 
    + ' missed guesses and ' 
    + str(len(correct_letters)) 
    + ' correct guesses, the word was "' 
    + secret_word + '"')


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
        print('Yes! The secret word is "' + secret_word + '"! You have won!')
    elif player_lost(): # if evaluation returns false, we need to know why 
        display_board(missed_letters, correct_letters, secret_word)
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