# Author: Nathan Asif | 2024F-BSE-278
# Take the marks of 5 courses from the user and calculate the average and percentage,   display the result:
# Eachcourse=50 marks
# Total_marks= course1+course2+course3+course4+course5
# average=Total_marks/5
# percentage=(Total_marks x 100)/25

pfund_th = eval(input("Enter marks for P-Fund Theory: "))
pfund_pr = eval(input("Enter marks for P-Fund Practical: "))
itc_th = eval(input("Enter marks for ITC Theory: "))
itc_pr = eval(input("Enter marks for ITC Practical: "))
fn_english = eval(input("Enter makes for Functional English: "))

totalMarks = 250
obtMarks = pfund_th + pfund_pr + itc_th + itc_pr + fn_english
# Calculate the percentage
percentage = (obtMarks / totalMarks) * 100
# Calculate the average
average = obtMarks / 5
print("\n----- Results -----") 
print(f"Total Marks:\t {totalMarks}") 
print(f"Obtained Marks:\t {obtMarks}") 
print(f"Average Marks:\t {average}") 
print(f"Percentage:\t {percentage}%")