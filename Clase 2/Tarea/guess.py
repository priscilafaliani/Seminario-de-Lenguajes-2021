from player import player_won


def is_valid_guess(guess, already_guessed):
    """Returns True if the guess is a valid input, otherwise returns False & prints the correct error message"""
    if len(guess) != 1:
        print('Please enter a single letter.')
    elif guess in already_guessed:
        print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a LETTER.')
    else:
        return True
    return False


def get_guess(already_guessed):
    """Returns a letter (in 'abcdefghijklmnopqrstuvwxyz') entered by the player."""
    while True:
        guess = input('Guess a letter: ').lower()
        if is_valid_guess(guess, already_guessed):
            return guess
            

def evaluate_guess(guess, missed_letters, correct_letters, secret_word):
    """"Returns True only if the player won the game, false otherwise
    
        Remember:
            The function returns False but doesn't specify if the player lost
            or was just another missed letter
    """
    global missed_letters, correct_letters

    if guess in secret_word:
        correct_letters += guess

        if player_won(secret_word, correct_letters):
            return True
    else:
        missed_letters += guess
        return False
