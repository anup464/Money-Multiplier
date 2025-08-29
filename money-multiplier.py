

# INPUT BY USER
initial_amount = int(input("Enter your initial amount: "))
multiplayer = int(input("Enter your multiplayer number: "))
days = int(input("Enter number of days:"))

# CALCULATION
total_amount = initial_amount *( multiplayer ** (days -1))


print("Total amount after", days, "days is:", total_amount)

