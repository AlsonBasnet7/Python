items = []

while True:
    user_input = input("write stop to complete your list: ")
    
    if user_input.lower() == "stop":
        break
    
    items.append(user_input)

print("Your list is:", items)