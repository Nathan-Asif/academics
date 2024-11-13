# Author: Nathan Asif | 2024F-BSE-278
# Calculate Distance Between Two Points (Pythagorean Theorem)

# Formula for "Distance = ((x2−x1)^2+(y2−y1)^2)^1/2"

# Defining coordinates of two points (x1, y1) & (x2, y2)
x1, y1 = 5, 15  # First point
x2, y2 = 10, 20 # Second point

# Calculating Distance
Distance = pow(pow((x2 - x1), 2) + pow((y2 - y1), 2), 1/2)

# Optional Enhancement rounding "round()" the result value to make it more readable
Distance = round(Distance, 2)

# Result
print(f"Distance = {Distance}")