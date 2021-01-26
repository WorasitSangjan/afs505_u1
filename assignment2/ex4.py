# Set the 'car' variable's value
cars = 100
# Set the 'space_in_a_car' variable's value
space_in_a_car = 4
# Set the 'drivers' variable's value
drivers = 30
# Set the 'passengers' variable's value
passengers = 90

# Start calcution using the variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Display the results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
