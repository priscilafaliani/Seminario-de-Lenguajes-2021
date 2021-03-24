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