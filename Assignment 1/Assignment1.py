# Assignment 1 - Module 2: Basic Python Concepts

# =========================
# Task 1: Mathematical Operations
# =========================
print("TASK 1: Basic Mathematical Operations")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nResults:")
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Cannot divide by zero.")

except ValueError:
    print("Please enter valid numeric values.")

# =========================
# Task 2: Personalized Greeting
# =========================
print("\nTASK 2: Personalized Greeting")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(f"Hello, {full_name}! Welcome to the Python Program.")
