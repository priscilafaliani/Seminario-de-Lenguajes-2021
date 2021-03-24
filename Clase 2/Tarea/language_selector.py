def invalid_input_message(language):
    """Shows a message indicating that the language is not supported.

        If language is an empty string, an invalid input prompt is shown.
    """

    if language:
        print(f'Error, the language {language} is not supported - Error, el lenguaje {language} no esta disponible')
    else:
        print('Invalid input. Try again with "english" or "español" - Input inválido. Intente de nuevo ingresando "english" o "español"')


def get_language_input():
    """Returns a language obtained from user input."""

    return (input('Language/Idioma (english - español): ')).lower()


# ---- MAIN ----

language = get_language_input()
# prompts the user until a valid input is given
while language != 'english' and language != 'español':
    invalid_input_message(language)
    language = get_language_input()


# Imports the words in the language choosen
if language == 'english':
    from words.english import *
else:
    from words.español import *

words = {
    'Colors': colors, 
    'Shapes': shapes, 
    'Fruits': fruits, 
    'Animals': animals
}