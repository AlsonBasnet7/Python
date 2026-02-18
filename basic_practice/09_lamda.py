# 3. Lambda Functions
# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The addition of the two number is",
      (lambda x, y: x + y)(num1, num2))

