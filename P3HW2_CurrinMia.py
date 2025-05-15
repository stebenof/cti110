# Mia Currin
# P3HW2
# 4/16/25
# Calculating employee gross pay

# Gather employee name, hours worked, pay rate

employee = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# OT variables
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
else:
    regular_hours = hours_worked
    overtime_hours = 0

# Calculate pay
reg_pay = regular_hours * pay_rate
ot_pay = overtime_hours * (pay_rate * 1.5)   #OT is 1.5 regular rate
gross_pay = reg_pay + ot_pay

# Insert breaking lines then display results - ensure proper alignment
print("\n------------------------------")
print("Employee name: ", employee)
print("Hours    Pay        OTime      OT Pay      RegHour Pay    Gross Pay\n-------------------------------")



print(f"{regular_hours}      ${pay_rate:.2f}      {overtime_hours}      ${ot_pay:.2f}      ${reg_pay:.2f}      ${gross_pay:.2f}")





