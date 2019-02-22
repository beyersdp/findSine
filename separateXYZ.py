'''
Separate given x, y and z file by value positions in an array
	
	- Input the 6 values over argv[i] ( i > 2)
	- Iterate over given x, y and z file argv[1]
	- Save the new files in given diretory of 
	  the participant (t1 to t6) argv[2]

	Code for the main experiment!
'''

import sys

print("\n[INIT] The separation values are:")
for i in range(3, 10):
	print("\t- " + sys.argv[i])



print("\n[Read] " + sys.argv[1] + "x.txt")
lineCount = 0
with open(sys.argv[1] + "x.txt", "r") as file_x:
	for line in file_x:
		if lineCount < int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t1/x.txt " + line)
			file_res_x1 = open(sys.argv[2] + "t1/x.txt", "a")
			file_res_x1.write(line)
			file_res_x1.close()

		if lineCount < int(sys.argv[5]) - int(sys.argv[3]) and lineCount > int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t2/x.txt " + line)
			file_res_x2 = open(sys.argv[2] + "t2/x.txt", "a")
			file_res_x2.write(line)
			file_res_x2.close()

		if lineCount < int(sys.argv[6]) - int(sys.argv[3]) and lineCount > int(sys.argv[5]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t3/x.txt " + line)
			file_res_x3 = open(sys.argv[2] + "t3/x.txt", "a")
			file_res_x3.write(line)
			file_res_x3.close()

		if lineCount < int(sys.argv[7]) - int(sys.argv[3]) and lineCount > int(sys.argv[6]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t4/x.txt " + line)
			file_res_x4 = open(sys.argv[2] + "t4/x.txt", "a")
			file_res_x4.write(line)
			file_res_x4.close()

		if lineCount < int(sys.argv[8]) - int(sys.argv[3]) and lineCount > int(sys.argv[7]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t5/x.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t5/x.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()
		
		if lineCount < int(sys.argv[9]) - int(sys.argv[3]) and lineCount > int(sys.argv[8]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t6/x.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t6/x.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()


		if lineCount > int(sys.argv[9]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t7/x.txt " + line)
			file_res_x6 = open(sys.argv[2] + "t7/x.txt", "a")
			file_res_x6.write(line)
			file_res_x6.close()

		lineCount += 1



print("\n[Read] " + sys.argv[1] + "y.txt")
lineCount = 0
with open(sys.argv[1] + "y.txt", "r") as file_x:
	for line in file_x:
		if lineCount < int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t1/y.txt " + line)
			file_res_x1 = open(sys.argv[2] + "t1/y.txt", "a")
			file_res_x1.write(line)
			file_res_x1.close()

		if lineCount < int(sys.argv[5]) - int(sys.argv[3]) and lineCount > int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t2/y.txt " + line)
			file_res_x2 = open(sys.argv[2] + "t2/y.txt", "a")
			file_res_x2.write(line)
			file_res_x2.close()

		if lineCount < int(sys.argv[6]) - int(sys.argv[3]) and lineCount > int(sys.argv[5]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t3/y.txt " + line)
			file_res_x3 = open(sys.argv[2] + "t3/y.txt", "a")
			file_res_x3.write(line)
			file_res_x3.close()

		if lineCount < int(sys.argv[7]) - int(sys.argv[3]) and lineCount > int(sys.argv[6]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t4/y.txt " + line)
			file_res_x4 = open(sys.argv[2] + "t4/y.txt", "a")
			file_res_x4.write(line)
			file_res_x4.close()

		if lineCount < int(sys.argv[8]) - int(sys.argv[3]) and lineCount > int(sys.argv[7]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t5/y.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t5/y.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()
		
		if lineCount < int(sys.argv[9]) - int(sys.argv[3]) and lineCount > int(sys.argv[8]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t6/y.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t6/y.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()

		if lineCount > int(sys.argv[9]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t7/y.txt " + line)
			file_res_x6 = open(sys.argv[2] + "t7/y.txt", "a")
			file_res_x6.write(line)
			file_res_x6.close()

		lineCount += 1


print("\n[Read] " + sys.argv[1] + "z.txt")
lineCount = 0
with open(sys.argv[1] + "z.txt", "r") as file_x:
	for line in file_x:
		if lineCount < int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t1/z.txt " + line)
			file_res_x1 = open(sys.argv[2] + "t1/z.txt", "a")
			file_res_x1.write(line)
			file_res_x1.close()

		if lineCount < int(sys.argv[5]) - int(sys.argv[3]) and lineCount > int(sys.argv[4]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t2/z.txt " + line)
			file_res_x2 = open(sys.argv[2] + "t2/z.txt", "a")
			file_res_x2.write(line)
			file_res_x2.close()

		if lineCount < int(sys.argv[6]) - int(sys.argv[3]) and lineCount > int(sys.argv[5]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t3/z.txt " + line)
			file_res_x3 = open(sys.argv[2] + "t3/z.txt", "a")
			file_res_x3.write(line)
			file_res_x3.close()

		if lineCount < int(sys.argv[7]) - int(sys.argv[3]) and lineCount > int(sys.argv[6]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t4/z.txt " + line)
			file_res_x4 = open(sys.argv[2] + "t4/z.txt", "a")
			file_res_x4.write(line)
			file_res_x4.close()

		if lineCount < int(sys.argv[8]) - int(sys.argv[3]) and lineCount > int(sys.argv[7]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t5/z.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t5/z.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()
		
		if lineCount < int(sys.argv[9]) - int(sys.argv[3]) and lineCount > int(sys.argv[8]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t6/z.txt " + line)
			file_res_x5 = open(sys.argv[2] + "t6/z.txt", "a")
			file_res_x5.write(line)
			file_res_x5.close()

		if lineCount > int(sys.argv[9]) - int(sys.argv[3]):
			print("[Write] " + sys.argv[2] + "t7/z.txt " + line)
			file_res_x6 = open(sys.argv[2] + "t7/z.txt", "a")
			file_res_x6.write(line)
			file_res_x6.close()

		lineCount += 1





