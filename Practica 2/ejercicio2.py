import re

def clear_string(line):
    """"Returns a string with all the non alphanumeric characters removed & lowercased.
    
        Parameters:
            - line : str
            The string to be cleared
    """
    return re.sub('[^\w\']', ' ', line).strip().lower()

def update_words(word, words):
    """If the word doesn't exist in the dict, it adds it. Else, increment the count.

        Ignores empty strings.

        Parameters:
            word : str
            The word to be registered/incremented

            words : dict -> {str(word): int(count)}
            Number of times a word appeared            
    """
    if word:
        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1


def update_max(words, word, max):
    """Updates the most seen word only if needed

        Ignores empty strings.
    
        Parameters:
            words : dict -> {str(word): int(count)}
            Number of times a word appeared            

            word : str
            Key to access the count of the word to be compared with the max

            max : dict -> {"word": str(word), "count": int(count)}
            List keeping the (currently) most used word and his appearences
    """
    if word:
        if words[word] > max["count"]:
            max["word"] = word
            max["count"] = words[word]

words = {}

max = {"word": '', "count": 0}

with open('Practica 2\\numpy_readme.txt', 'r') as numpy_readme:
    for line in numpy_readme:

        # get a list with the words (ignores blank lines)
        if line != '\n':            
            current_words = clear_string(line).split(' ')

            # count
            for word in current_words:
                update_words(word, words)
                update_max(words, word, max)

print(max)