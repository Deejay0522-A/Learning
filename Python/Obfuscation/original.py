from random import randint as rint
from random import shuffle

helloWorld = "Hello, World!"
password = str(input("Enter a password: "))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0', '!', '@', '#', '$', '%', '&', '*', '?', '-', '_', '+', '=', '~']

def Cypher(Item : str, Library : list):
    hashing = []
    newPass = ""
    oldPassword = list(Item)
    while len(oldPassword) > 0:
        choice = rint(1,2)
        if choice == 1:
            hashing.append(Library[rint(0, len(Library)-1)])
        else:
            hashing.append(oldPassword.pop(rint(0,len(oldPassword)-1)))

    for char in hashing:
        newPass = newPass + char
    return newPass

print(helloWorld)
print(Cypher(password, alphabet))