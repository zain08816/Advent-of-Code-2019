

INPUT = '307237-769058'



def check_password(passw):
	passw = list(map(int, list(str(passw))))

	print(passw)

	for i in range(1, len(passw)):
		if passw[i] < passw[i-1]:
			return False
	value = False
	for x in range(0,5):
		if passw[x] == passw[x+1] :
			if(x <= 3):
				if passw[x+1]!=passw[x+2] :
					if x>=1 :
						if passw[x] != passw[x-1] :
							value = True
						else:
							value = True
			else:
				if passw[x] != passw[x-1] :
					value = True
	return value



count = 0
for i in range(307237, 769059):
	if check_password(i):
		count += 1

print(count)

print(sum([sum([1 if str(p).count(c)==2 and sum([1 if str(p)[i]==c and str(p)[i+1]==c else 0 for i in range(0,5)])else 0 for c in '123456789'])and min([1 if str(p)[i]<=str(p)[i+1] else 0 for i in range(0, 5)]) for p in range(307237, 769059)]))