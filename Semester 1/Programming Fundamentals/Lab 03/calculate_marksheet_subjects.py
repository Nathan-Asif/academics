# Author: Nathan Asif | 2024F-BSE-278
# Calculate a Marksheet of 5 Subjects and print the Total Marks & Percentage

def calculate_marksheet(subjects):
    total_marks = 500
    obtained_marks = sum(subjects.values())
    percentage = (obtained_marks / total_marks) * 100

    print("Subject-wise Marks:")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    print(f"\nTotal Marks: {total_marks}")
    print(f"Obtained Marks: {obtained_marks}")
    print(f"Percentage: {percentage:.2f}%")

subjects = {
    "Programming-Fundamentals": 80,
    "ITC": 72,
    "Functional-English": 84,
    "Programming-Fundamentals-Lab": 83,
    "ITC-Lab": 75
}

calculate_marksheet(subjects)