chain = open("day02_input.txt", "r");

for l in chain:
	code = l

code = list(map(int, code.split(',')))
print(code)
i = 0
while i < len(code):
	a, b, c, d  = code[i:i+4];
	if a == 99:
		break
	if a == 1:
		code[d] = code[b]+code[c]
	if a == 2:
		code[d] = code[b]*code[c]
	print(a, b, c, d)
	i += 4
print(code)