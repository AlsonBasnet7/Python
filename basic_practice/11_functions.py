# Function Arguments & Return Values
# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)
def firstlast(name, caste):
    # name=input("Enter your name")
    # caste=input("Enter your caste")
    return name+" "+caste
name=input("Enter your name : ")
caste=input("Enter your caste : ")
print("Your first and last name is", firstlast(name,caste))
