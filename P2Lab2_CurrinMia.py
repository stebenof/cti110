#Mia Currin
#4/9/25
#P2Lab2
#Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':100, 'Silverado':26}

#Get keys from dict
cars_keys = cars.keys()

print(cars_keys)


print(*cars_keys, sep = ",")

#Get name of car from user
car_name = input("Enter a car: ")

#Display mpg for car given
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get number of miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#Calculate gallons of gas needed for input car and mileage
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")

