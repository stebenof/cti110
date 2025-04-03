#Mia Currin
#4/2/25
#P1HW2
#Program to calculate travel expenses

print('This program calculates and displays travel expenses.')
print('Enter Budget:', end=' ')
budget=int(input())
print('Enter your travel destination:', end='   ')
destination=input()
print('How much do you think you will spend on gas?', end='  ')
gas=int(input())
print('Approximately, how much will you need for accomodation/hotel?', end=' ')
hotel=int(input())
print('Last, how much do you need for food?', end=' ')
food=int(input())
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Intial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print()

#To get the remaining balance, you will subtract the sum of 'gas', 'hotel', and 'food' from the intial budget ('budget')

print('Remaining Balance:', budget-(gas+hotel+food))
