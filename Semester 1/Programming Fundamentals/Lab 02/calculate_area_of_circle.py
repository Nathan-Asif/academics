# Author: Nathan Asif | 2024F-BSE-278
# Calculate the area of a circle

# Constant pie "π" value
P = 3.14

# Radius Value
r = 50

# Formula: A = π * r^2 | A=πr²
# pow() "function" or ** "double asterisk" is used to calculate the power of a base
A = P * pow(float(r), 2)

# Result
print(f"Area of Circle = {A}")