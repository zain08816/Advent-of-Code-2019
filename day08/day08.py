import re

stream = open('day08.txt', 'r')

image = ''
for i in stream:
	image = i.replace('\n', '')

#print(image)

seg = []
x = 0
while x < len(image):
	seg.append(image[x:x+150])
	x += 150


counts = []
for i in seg:
	counts.append(i.count('0'))


print(counts)

m = 9999999999
low_index = 0
for x in range(len(counts)):
	if counts[x] < m:
		m = counts[x]
		low_index = x

print(m)
print(low_index)

print(seg[low_index].count("2")*seg[low_index].count("1"))

print(seg[low_index])

# print(seg)
# print(len(seg[0]))
# print(len(image))
