from hangman_functions import getRandomWord, displayBoard, getGuess, playAgain
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
        

print('H A N G M A N')

set_difficulty()

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break