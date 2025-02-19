#Pythagorean theorem for find the hypotenuse area value
import math

a = float(input("Enter the side A value : "))
b = float(input("Enter the side B value : "))

c = math.sqrt(pow(a, 2) + pow(b,2))

print(f"Side C value is = {c}")