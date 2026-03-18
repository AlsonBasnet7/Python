names = []
marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    
    names.append(name)
    marks.append(mark)

highest = marks[0]
lowest = marks[0]
total = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    total = total + m

average = total / n

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Grade:", grade)