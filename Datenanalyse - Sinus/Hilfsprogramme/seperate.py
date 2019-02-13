

num = 1
change = False

with open("dataOUT.txt", "r") as fileY, open("z.txt", "r") as fileZ:
	for y, z in zip(fileY, fileZ):
		#print(y.strip(), z.strip())
		if float(z.strip()) > 35.93:
			print("[" + str(num) + "]" + " " + y.strip() + " " +z.strip())
			change = False
			erg = open(str(num) + ".txt", "a")
			erg.write(y.strip() + "\n")
			erg.close()
		else:
			if change == False:
				change = True
				num += 1
			
						