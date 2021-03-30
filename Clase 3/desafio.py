def caesar_cipher(phrase, key=1):
    return ''.join(map(lambda c: chr(ord(c) + key), phrase))

print(caesar_cipher('a'))
print(caesar_cipher('ABC'))
print(caesar_cipher('Rock2021'))