# Hadrien Howard
# P2HW2
# 10/1/2026
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

grade1 = float(input("enter score 1: "))
grade2 = float(input("enter score 2: "))
grade3 = float(input("enter score 3: "))
grade4 = float(input("enter score 4: "))
grade5 = float(input("enter score 5: "))
grade6 = float(input("enter score 6: "))

# put the grades in a list
grades_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# get the lowest grade in the list
print(f"lowest grade: {min(grades_list)}")

# get the highest grade
print(f"highest grade: {max(grades_list)}")

# get the sum of all grades
print(f"sum of grades: {sum(grades_list)}")

average = sum(grades_list) / len(grades_list)

print(f"average grade: {average:.1f}")