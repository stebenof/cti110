#Mia Currin
#4/9/25
#P2HW1
#Nicer formatting using strings

#Enter expenses using float strings

print('This program calculates and displays travel expenses: ')

budget = float(input('\nEnter budget: '))

destination = (input('\nEnter your travel destination: '))

gas = float(input('\nHow much do you think you will spend on gas? '))

hotel = float(input('\nApproximately, how much will you need for accommodation/hotel? '))

food = float(input('\nLast, how much do you need for food? '))

#Calculate to two decimal points, aligned 

print('\n------------Travel Expenses------------')
print(f'Location:           {destination}')
print(f'Initial budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodation:       ${hotel:.2f}')
print(f'Food:               ${food:.2f}')
print('----------------------------------------')

#Display remaining balance

remaining_bal = budget - gas - hotel - food
print(f'\nRemaining Balance:  ${remaining_bal:.2f}')


