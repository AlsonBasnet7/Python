# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)
def calculate_area(length, width=10):
    return length*width
length=int(input("Enter the length"))
print("The area is",calculate_area(length,width=10))