#input values
    #What are input values?
        #input values are string variables that have a determined value based on what you input into the terminal

#example
inputVal = input("What would you like to say? \n") #the \n is a new line

print(inputVal)

#Say you want to change the value of an input
newInput = input("Enter a number: ")

newInput = int(newInput) #this changes the input string to an integer through a method called "Casting"
#Casters
    #int()
    #str()
    #float()
print("Your new value is:", newInput + 5) #adding 5 to the value