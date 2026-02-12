#Print Statments
    #What are print statements?
        #Print statments are methods used to output a value within a terminal

#examples
print("Hello World!")

#Say you want to add a value to your print()
value = 10

print("hello the number ten in numbers is", value) #The comma allows for more items to print through a process called "concatnation" 

#concatnators
    #print(val [,] val2)
    #print(val [+] val2) this does not add a space, be aware
    #print(f"String {value}") this is called an "f string", this allows you to input values to a string using {}. This will substitute the space given for any values inputed and will output the print the same as it looks.

#example of f string
age = None #make this an integer
print(f"Hello world! My age is {age}.")

age = 10

helloWorld = "Hello World"
print(f"Hello world! My age is {age}. {helloWorld}")