def fuel_function(weight):
	return (weight//3)-2

weights = open("day01_input.txt", "r");

total = 0

for weight in weights:
	int_weight = int(weight)
	total += fuel_function(int_weight)
	print(total)

print("sum of fuel requirements: " + str(total))
