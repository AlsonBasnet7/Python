numbers = [1,1,2,3,3,4,4,5,6,5,6]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)