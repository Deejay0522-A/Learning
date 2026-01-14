import math

#C^2 = A^2 + B^2 - 2ab * cos(<)

#while loop var
loop = True

#variables for the equation
a = float(input("What is A? "))
b = float(input("What is B? "))
angle = input("What is the angle? ")
c = input("What is the C? ")

#Chooses how to go about on whats missing
if c == "None" or c == "none":
    angle = float(angle)
    c = float(a**2 + b**2 - 2*a*b*math.cos(angle))

    print(f"Your answer is: {math.sqrt(c)}")

if angle == "None" or angle == "none":
    c = float(c)

    #A^2 + B^2
    ab = float(a**2 + b**2)
    print(f"AB = {ab}")

    #2ab * cosBeta
    ab2 = float(2*a*b)
    print(f"2ab = {ab2 * -1}")

    #C^2
    c2 = c**2
    print(f"C^2 = {c2}")

    #C - (A^2 + B^2)
    cMinusab = float(c2 - ab)
    print(f"C is now {cMinusab}")

    #newC / ab2
    arcCosReady = float((cMinusab / ab2) * -1)
    print(f"C divided by -2ab = {arcCosReady}")

    
    arcCos = float(math.acos(arcCosReady))
    print(f"Your answer is: {arcCos}")
