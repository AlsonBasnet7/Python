n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

for i in range(n):
    print(a)
    a, b=b, a+b
arr=[5,3,5,2]
n=len(arr)
for i in range(n):
    for j in range (0,n-i-1):
        if arr[j]>arr[i+1]:
            arr[j],arr[j+1]=
arr = [5, 3, 8, 1]
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)