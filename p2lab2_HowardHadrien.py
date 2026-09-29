# Hadrien Howard
# p2Lab2

#  write code that uses a dictionary to store user input and displays output to the user

# write dictionary where each car name is a key and their MPG is the value
vehicles = {
    "camaro": 18.21,
    "prius": 52.36,
    "model s": 110,
    "silverado": 26
}

# store all dictionary keys in a variable
keys = vehicles.keys()

    # print the vehicle names for each user
print(keys)
    
    # ask the user to input a vehicle name
vehicle = input("enter a vehicle name to see its MPG: ")

# use the vehicle name entered by the user to get its MPG
mpg = vehicles[vehicle]

# display the MPG for vehicle selected
print(f"the {vehicle} gets {mpg} mpg. ")

# ask the user how many miles they want to go
miles = float(input(f"how many miles will you drive the {vehicle}? "))

# calculate gallons needed, divide miles driven by the vehicles MPG
gallons_needed = miles/mpg

# display the result, round by 2 decimal places
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles. ")