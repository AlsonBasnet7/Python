n = int(input("Enter N: "))

fib = [1, 1]

for i in range(2, n):
    next_num = fib[i-1] + fib[i-2]
    fib.append(next_num)

print(fib)