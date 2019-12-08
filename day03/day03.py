f = open("day03.txt", "r")

x = []
for i in f:
	x.append(i)
A = x[0].split(',')
B = x[1].split(',')


print(A)
print(B)

def toCenter(num1, num2):
	distance =abs(num1) + abs(num2)
	return distance

a_map = {}
x = 0
y = 0
step = 0
for i in A:
	d = i[0]
	l = int(i[1:])

	if d == 'R':
		for _ in range(1, l+1):
			x += 1
			step += 1
			if (x, y) in a_map:
				continue
			a_map[(x, y)] = step
			

	if d == 'L':
		for _ in range(1, l+1):
			x -= 1
			step += 1
			if (x, y) in a_map:
				continue
			a_map[(x, y)] = step


	if d == 'U':
		for _ in range(1, l+1):
			y += 1
			step += 1
			if (x, y) in a_map:
				continue
			a_map[(x, y)] = step


	if d == 'D':
		for _ in range(1, l+1):
			y -= 1
			step += 1
			if (x, y) in a_map:
				continue
			a_map[(x, y)] = step


print(a_map)

b_map = {}
x = 0
y = 0
step = 0
for i in B:
	d = i[0]
	l = int(i[1:])

	if d == 'R':
		for _ in range(1, l+1):
			x += 1
			step += 1
			if (x, y) in b_map:
				continue
			b_map[(x, y)] = step
			

	if d == 'L':
		for _ in range(1, l+1):
			x -= 1
			step += 1
			if (x, y) in b_map:
				continue
			b_map[(x, y)] = step


	if d == 'U':
		for _ in range(1, l+1):
			y += 1
			step += 1
			if (x, y) in b_map:
				continue
			b_map[(x, y)] = step


	if d == 'D':
		for _ in range(1, l+1):
			y -= 1
			step += 1
			if (x, y) in b_map:
				continue
			b_map[(x, y)] = step

print(a_map)

intersect = {}
for coord in a_map:
	if coord in b_map:
		intersect[coord] = a_map[coord] + b_map[coord]

print(intersect)

low = 9999999999999999999
close = ()
# for i in intersect:
# 	dist = toCenter(i[0], i[1])
# 	if dist < low:
# 		low = dist
# 		close = i

for i in intersect:
	dist = intersect[i]
	if dist < low:
		low = dist

print(close)
print(low)


