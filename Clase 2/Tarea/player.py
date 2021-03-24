from pictures import HANGMAN_PICS


def player_won(secret_word, correct_letters):
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letters:
            return False
    return True


def player_lost(missed_letters):
    return len(missed_letters) == len(HANGMAN_PICS) - 1
