import random
from random import randint as rint

def encrypt(message: str, shift):
    result = "" 
    for char in message:
        if char.isalpha():
            ascii_off = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_off + shift)
            result += chr(ascii_off + shifted)
        else:
            result += char
    return result

messageEncrypt = encrypt(input("Password: "), 3)

print(messageEncrypt)