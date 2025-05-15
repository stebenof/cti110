# Mia Currin
# P4LAB2
# 4/30/25
# Using 'while' loop and 'for' loop


# Loop statement

runagain = "yes"



while runagain.lower() == "yes":
    
    number = int(input("Enter an integer: "))
    print("\n")
    
    if number >= 0:
        for i in range(1, 12 + 1):
            print(f"{number} * {i} = {number * i}")
        print("\n")
    else:
        print("This program does not handle negative numbers")
        print("\n")
        
    runagain = input("Would you like to run the program again? Enter yes or no: ")
    print("\n")
    
#This happens after the loop breaks
print("Exiting program...")
