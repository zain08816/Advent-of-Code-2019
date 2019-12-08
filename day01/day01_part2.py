def fuel_function(weight):
	return ((weight//3)-2)

weights = open("day01_input.txt", "r");

total = 0

for weight in weights:
	int_weight = int(weight)
	remainder = fuel_function(int_weight)
	running_cost = remainder
	while True:
		remainder = fuel_function(remainder)
		if remainder <= 0:
			break
		running_cost += remainder
	total += running_cost

print("sum of fuel requirements: " + str(total))
