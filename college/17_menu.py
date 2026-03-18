# Simple Price Calculator

prices = []

n = int(input("How many items? "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    prices.append(price)

total = sum(prices)
average = total / n

print("\n--- Result ---")
print("Total Price:", total)
print("Average Price:", average)
print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))