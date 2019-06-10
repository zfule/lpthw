cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")#这有多少可用车
print("There are only", drivers, "drivers available.")#这有多少可用司机
print("There will be", cars_not_driven, "empty cars today.")#今天将有多少空车
print("We can transport", carpool_capacity, "people today")#今天我们可运送多少人
print("We have", passengers, "to carpool today.")#今天拼车有多少人
print("We need to put about", average_passengers_per_car, "in each car.")#每辆车放多少人
