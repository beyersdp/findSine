count = 0
gab = False

with open ("z.txt", "r") as fileZ:
	for line in fileZ:
		if float(line) < 35.93:
			if gab == False:
				count += 1
				gab = True
		else:
			if gab == True:
				gab = False

print(count)