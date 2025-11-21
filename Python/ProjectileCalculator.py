# How to solve for the different factors of projectile motion
import math

# Define known variables
# For this example, we have Feta, Normal Veloctity, and Final Y Velocity
feta = 20
normalVelocity = 40
finalYVelocity = 0

# How to calculate the Initial Velocity for Y axis
#use Viy = V * sin(feta)
initialYVelocity = normalVelocity * math.sin(feta)
print("Initial Y Velocity:", initialYVelocity)

# Calculating time
# Use Vfy = g * t + Viy
gravity = -10

#Use inverse operations to isolate t
# Vfy - Viy = g * t
# Vfy / g = t
t = (finalYVelocity - initialYVelocity) / gravity
print("Time:", t)

# Calculating displacement in Y axis
# Use DeltaY = Viy * t + (g/2) * t^2
displacementY = initialYVelocity * t + (gravity / 2) * t**2
print("Displacement Y:", displacementY)

# Calculating Initial Velocity for X axis
# Use Vix = V * cos(feta)
initialXVelocity = normalVelocity * math.cos(feta)
print("Initial X Velocity:", initialXVelocity)

# Calculating displacement in X axis
# Use DeltaX = Vix * t
displacementX = initialXVelocity * t

#You can use the same equations to find the same variables mentioned in each equation used if you isolate the variable you want to find