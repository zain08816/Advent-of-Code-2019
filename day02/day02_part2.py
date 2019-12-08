
chain = open("day02_input.txt", "r");

for l in chain:
	master_code = l

code = list(map(int, master_code.split(',')))
print(master_code)

pivotal = 19690720

def test_answer(j, k, code):
	code[1] = j
	code[2] = k
	i = 0
	while i < len(code):
		a, b, c, d  = code[i:i+4];
		if a == 99:
			break
		if a == 1:
			code[d] = code[b]+code[c]
		if a == 2:
			code[d] = code[b]*code[c]
		#print(a, b, c, d)
		i += 4
	return code[0]

found = False
for j in range(99):
	for k in range(99):
		#print(j, k)
		code = list(map(int, master_code.split(',')))
		x = test_answer(j, k, code)
		#print(x)
		if x == pivotal:
			found = True
			print(100 * j + k)
			break
	if found == True:
		break