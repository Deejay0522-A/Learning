def the_big_question(x,y):
    print(f"Computer, is {num1} the same as {num2}?\n{x == y}")
    print(f"Computer, is {num1} different from {num2}? \n{x!=y}")

num1 = input("Give me a thing: ")
num2 = input("Give me a thing: ")
the_big_question(num1, num2)