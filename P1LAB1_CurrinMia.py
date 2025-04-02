#Mia Currin
#4/2/2025
#P1HW1
#Create program to do basic arithmetic functions

print('-----Calculating Exponents----')
print()
print('Enter an integer as the base value:', end='    ')
base_value=int(input())

print('Enter an integer as the exponent:', end='    ')
exponent_value=int(input())
print()
print(base_value, 'raised to the power of', exponent_value, 'is', base_value**exponent_value, '!!')
print()
print('-----Addition and Subtraction----')
print()
print('Enter a starting integer:', end='    ')
starting=int(input())
print('Enter an integer to add:', end='    ')
add_num=int(input())
print('Enter an integer to subtract:', end='    ')
sub_num=int(input())
print()
print(starting, '+', add_num, '-', sub_num, 'is equal to', starting+add_num-sub_num)

