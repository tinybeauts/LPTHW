cars = 100 # number of cars
space_in_a_car = 4 # number of people that can fit in a car
drivers = 30 # number of drivers
passengers = 90 # number of people who need to get somewhere
cars_not_driven = cars - drivers # number of cars not driven because there are more cars than drivers
cars_driven = drivers # number of cars that can be driven
carpool_capacity = cars_driven * space_in_a_car # maximum number of people that can be driven
average_passengers_per_car = passengers / cars_driven # average number of people that need to be in each car to fit everyone.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."