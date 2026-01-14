import math

def AnnualToHour(annual, hours):
    yearlyWeekHours = hours * 52

    hourlyRate = annual / yearlyWeekHours
    return hourlyRate

loop = True

while loop:
    gen = input("Do you want to run? ")

    if gen == "Yes" or gen == "yes":
        annual = int(input("Annual Rate: "))
        hours = int(input("Hours: "))
        
        print(AnnualToHour(annual, hours))
    
    elif gen == "No" or gen == "no":
        loop = False
        break

    else:
        print("Not an option.")
        continue