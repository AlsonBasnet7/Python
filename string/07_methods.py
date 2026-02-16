# Take the string "  i love python programming  " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Check if the string "123abc" is alphanumeric.
string="    i love programming"
spaces=string.strip()
print("The output is",spaces.capitalize())
print(spaces.isalnum())

