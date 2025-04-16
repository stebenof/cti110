# Mia Currin
# P3LAB1
# 4/16/25
# Branching - calculating most efficient number of dollars, quarters, dimes, nickels, and peenies needed to make a given amount

# Area to enter monetary amount
amount = float(input("Enter the amount of money: $"))

# Convert number to cents
cents = int(round(amount * 100))

# Dollars conversion
dollars = cents // 100
cents %= 100

# Quarters conversion
quarters = cents // 25
cents %= 25

# Dimes conversion
dimes = cents // 10
cents %= 10

# Nickels conversion
nickels = cents // 5
cents %= 5

# Pennies will be rest of cents
pennies = cents

# Results

if dollars != 0:
   print("No change")
else:
    print("")
    

if dollars > 0:
    if dollars == 1:
       print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")
if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if nickels == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")



    

