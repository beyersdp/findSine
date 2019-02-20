import sys

print("\n[Divide] Search value for Z to seperate X or Y in 18 parts...")
parts = 0
gab = False
div = 40
find = False

while div > 10:
	with open (sys.argv[1], "r") as fileZ:
		for line in fileZ:
			if float(line[:-1].replace(",",".")) < div:
				if gab == False:
					parts += 1
					gab = True
			else:
				if gab == True:
					gab = False
	
	if parts == 5:
		find = True
		break
	else:
		div -= 0.01
		parts = 0

if find:
	print("[Divide] For Z = {} the X or Y data is dividable in 18 parts".format(div))
else:
	print("[Divide][ERR] No Z found to divide X or Y data in 18 parts")
	sys.exit(1)



print("\n[Separate] Write data of X or Y in unique files, if Z falls under {}...".format(div))
num = 1
change = False

with open(sys.argv[2], "r") as fileY, open(sys.argv[1], "r") as fileZ:
	for y, z in zip(fileY, fileZ):
		#print(y.strip(), z.strip())
		if float(z[:-1].strip().replace(",",".")) > div:
			change = False
			erg = open(sys.argv[3] + str(num) + ".txt", "a")
			erg.write(y.strip() + "\n")
			erg.close()
		else:
			if change == False:
				change = True
				num += 1

print("[Seperate] Finished")
