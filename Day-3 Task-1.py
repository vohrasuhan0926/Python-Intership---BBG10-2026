# 1. Prices above the average price using list comprehension
prices = [120, 450, 80, 999, 250, 600, 150, 320, 750, 410]
avg_price = sum(prices) / len(prices)
above_avg = [p for p in prices if p > avg_price]
print("1. Average:", avg_price, "| Above average:", above_avg)

# 2. Convert full names to title case using list comprehension
names = ["riya sharma", "aman gupta", "suhan vahora", "sara khan"]
title_names = [name.title() for name in names]
print("2. Title Case Names:", title_names)

# 3. Remove duplicates while keeping original order (without set())
random_nums = [12, 45, 12, 89, 34, 45, 67, 89, 90, 23, 34, 56, 78, 10, 90]
unique_nums = []
for num in random_nums:
    if num not in unique_nums:
        unique_nums.append(num)
print("3. Without duplicates:", unique_nums)

# 4. Transpose of a 3x3 matrix using nested list comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("4. Transpose Matrix:", transpose)

# 5. Sort list of tuples by marks (topper first) using key parameter
students = [("Riya", 88), ("Aman", 95), ("Sara", 72), ("Zoya", 91)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("5. Topper first:", sorted_students)

# 6. Second largest number without using max() or min()
nums = [45, 89, 12, 95, 67, 95, 34]
largest = float('-inf')
second_largest = float('-inf')
for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n
print("6. Second largest:", second_largest)

# 7. Print employee names with salaries using zip()
employees = ["Riya", "Aman", "Sara", "Kabir"]
salaries = [35000, 42000, 38000, 45000]
print("7. Employee Salaries:")
for emp, sal in zip(employees, salaries):
    print(f"   {emp}: Rs.{sal}")
    

# 8. Small To-Do List Manager
todo_list = []

# Adding 5 tasks
todo_list.append("Learn Python variables")
todo_list.append("Practice Python Lists")
todo_list.append("Write a loop programs")
todo_list.append("Fix syntax errors in code")
todo_list.append("Upload assignments to GitHub")

# Removing 2 tasks by name
todo_list.remove("Fix syntax errors in code")
todo_list.remove("Upload assignments to GitHub")

# Printing current tasks
print("8. Current To-Do List:", todo_list)