# Mia Currin
# 4/9/25
# P2HW2
# Grade averages

#Ask user to import their test grades
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

#Store info on a list
gradeList = [] 
gradeList = [mod1, mod2, mod3, mod4, mod5, mod6]

#Determine lowest, highest, total, and average
lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
average = total / len(gradeList)

#Print results
print("\n ------------Results------------")
print(f'{"Lowest Grade:":<20}{lowest}')
print(f'{"Highest Grade:":<20}{highest}')
print(f'{"Sum of Grades:":<20}{total}')
print(f'{"Average:":<20}{average:.2f}')
print('-'*40)
