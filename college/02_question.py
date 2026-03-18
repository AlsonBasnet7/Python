n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("List:", numbers)
print("Maximum:", max_num)
print("Minimum:", min_num)