# This program calculates and finds the distance between 2 points based on the user's inputs.
# 1st of all, we need to import the math module in order to use the sqrt and pow functions.
import math

# The program then asks the user to input the coordinates of 2 points
x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))

# It then calculates the distance between the 2 points and then prints the result
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("The distance between the 2 points is", distance)
