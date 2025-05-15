# Mia Currin
# P4HW2
# 4/30/25
# Take P3HW2 and use loops to calculate different payment amounts




# Get employee information
done='"Done"' 

name=input(f"Enter employee's name or {done} to terminate: ")
stop=["Done", "done", "D", "d"]
employees=[]
over_total=[]
reg_total=[]
gross_total=[]

while name not in stop:
    hours=float(input(f"How many hours did {name} work? "))
    rate=float(input(f"What is {name}'s pay rate? "))
    print()
    print(f"Employee name: {name}")
    print()

    #Calculate pay
    if hours>40:
        over=hours-40
        over_pay=rate*1.5*over
        pay=(hours-over)*rate
    else:
        over=0
        over_pay=0
        pay=rate*hours
    gross=pay+over_pay

    #Display information
    print(f"{'Hours Worked':<14} {'Pay Rate':<14} {'OverTime':<14} {'OverTime Pay':<19} {'RegHour Pay':<19} {'Gross Pay'}")
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"{hours:<14} ${rate:<13,.2f} {float(over):<14} ${over_pay:<18,.2f} ${pay:<18,.2f} ${gross:,.2f}")

    employees.append(name)
    over_total.append(over_pay)
    reg_total.append(pay)
    gross_total.append(gross)
    print()
    name=input(f"Enter employee's name or {done} to terminate: ")
    
print(f"Total number of employees entered: {len(employees)}")
print(f"Total amount paid for ovetime: ${sum(over_total):,.2f}")
print(f"Total amount paid for regular hours: ${sum(reg_total):,.2f}")
print(f"Total amount paid in gross: ${sum(gross_total):,.2f}")
