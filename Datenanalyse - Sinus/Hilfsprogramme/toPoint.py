with open("z.txt", "r") as fileIN:
	with open ("z2.txt", "w") as fileOUT:
		for line in fileIN:
			print(line.replace(",", "."))
			fileOUT.write(line.replace(",", "."))