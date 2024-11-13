# Author: Nathan Asif | 2024F-BSE-278
# Convert Height (in feet and inches) into Centimeters

# Initial Feet and Inches Value
feet = 5
inches = 2

# Step 1: Convert feet to inches: feet x 12 inches
converted_inches = feet * 12

# Step 2: Add up the inches with converted inches
final_inches = converted_inches + inches

# Step 3: Convert inches to centimeters(cm) = inches x 2.54cm/inch
cm = final_inches * 2.54

# Result
print(f"{feet} feet {inches} inches = {cm}cm")