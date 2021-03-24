import random
from pictures import HANGMAN_PICS

def get_random_word(wordDict):
    """This function returns a random string from the passed dictionary of lists of strings, and the key also."""
    
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

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


def is_valid_guess(guess, alreadyGuessed):
    """Returns True if the guess is a valid input, otherwise returns False & prints the correct error message"""
    if len(guess) != 1:
        print('Please enter a single letter.')
    elif guess in alreadyGuessed:
        print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a LETTER.')
    else:
        return True
    return False


def get_guess(alreadyGuessed):
    """Returns a letter (in 'abcdefghijklmnopqrstuvwxyz') entered by the player."""
    while True:
        guess = input('Guess a letter: ').lower()
        if is_valid_guess(guess, alreadyGuessed):
            return guess


def play_again():
    """returns True if the player wants to play again, otherwise it returns False"""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')