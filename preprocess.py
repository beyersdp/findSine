'''
-------------------------------------------------------------------------
|	Project			: findSine											|
|	Program name	: preprocess.py										|
|	Author			: P. Beyersdorffer									|
|	Date created	: 12.02.2019 (13:00:59)       						|
|	Purpose			: extract three sine waves by indicator				|
|	Dependencies    : Input File paths and num Values					|
-------------------------------------------------------------------------
'''


import sys



filePathXY = input("\n[INIT] Enter file name with X or Y data: ")
filePathZ = input("[INIT] Enter file name with Z data: ")
numValues = int(input("[INIT] Enter number of values: "))



print("\n[ToPoint] Replacing Comma with Point...")
print("[ToPoint] For X or Y data...")

with open(filePathXY, "r") as fileIN:
	with open ("dataXY.temp", "w") as fileOUT:
		for line in fileIN:
			fileOUT.write(line.replace(",", "."))
			
print("[ToPoint] For Z data...")

with open(filePathZ, "r") as fileIN:
	with open ("dataZ.temp", "w") as fileOUT:
		for line in fileIN:
			fileOUT.write(line.replace(",", "."))


			
print("\n[Count] Check number of values in X or Y data...")
count = 0
with open ("dataXY.temp", "r") as file:
	for line in file:
		count += 1
if count != numValues:
	print("[Count][ERR] Number of values in X or Y data not corresponding (count = " +  str(count) + ")")
	sys.exit(1)
	
print("[Count] Check number of values in Z data...")
count = 0
with open ("dataZ.temp", "r") as file:
	for line in file:
		count += 1
if count != numValues:
	print("[Count][ERR] Number of values in Z data not corresponding (count = " +  str(count) + ")")
	sys.exit(1)

print("[Count] Number of values corresponding with " + str(numValues))



print("\n[Divide] Search value for Z to seperate X or Y in three parts...")
parts = 0
gab = False
div = 40
find = False

while div > 10:
	with open ("dataZ.temp", "r") as fileZ:
		for line in fileZ:
			if float(line) < div:
				if gab == False:
					parts += 1
					gab = True
			else:
				if gab == True:
					gab = False
	
	if parts == 2:
		find = True
		break
	else:
		div -= 0.01
		parts = 0

if find:
	print("[Divide] For Z = {} the X or Y data is dividable in three parts".format(div))
else:
	print("[Divide][ERR] No Z found to divide X or Y data in three parts")
	sys.exit(1)

	
	
print("\n[Separate] Write data of X or Y in unique files, if Z falls under {}...".format(div))
num = 1
change = False

with open("dataXY.temp", "r") as fileY, open("dataZ.temp", "r") as fileZ:
	for y, z in zip(fileY, fileZ):
		#print(y.strip(), z.strip())
		if float(z.strip()) > div:
			change = False
			erg = open(str(num) + ".txt", "a")
			erg.write(y.strip() + "\n")
			erg.close()
		else:
			if change == False:
				change = True
				num += 1

print("[Seperate] Finished")



count = 0
with open ("1.txt", "r") as file:
	for line in file:
		count += 1
print("\n[Results]  1.txt with {} values".format(count))

count = 0
with open ("2.txt", "r") as file:
	for line in file:
		count += 1
print("\n[Results]  2.txt with {} values".format(count))

count = 0
with open ("3.txt", "r") as file:
	for line in file:
		count += 1
print("\n[Results]  3.txt with {} values".format(count))