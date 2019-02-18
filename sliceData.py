'''
Load x,y,z data by input the number of the data set
Let user input the number of values for cut of
Iterate over files and save after passing the cutting value
Save valid values in file with name number without leading zeros
'''

file_number = input("ENTER number of the x,y,z files: ")
cut_number = int(input("ENTER number of non valid values: "))

if file_number[1] == "0":
    file_new = file_number[2:]
else:
    file_new = file_number[1:]



checksum_x = 0
checksum_y = 0
checksum_z = 0

# Generate checksum over x
with open("./data/xyz/" + file_number +  "x.csv", "r") as x_IN:
    for line in x_IN:
        checksum_x += 1
print("[CHECK] {} values in {}x.csv".format(checksum_x, file_number))

# Generate checksum over y
with open("./data/xyz/" + file_number +  "y.csv", "r") as y_IN:
    for line in y_IN:
        checksum_y += 1
print("[CHECK] {} values in {}y.csv".format(checksum_y, file_number))

# Generate checksum over z
with open("./data/xyz/" + file_number +  "z.csv", "r") as z_IN:
    for line in z_IN:
        checksum_z += 1
print("[CHECK] {} values in {}z.csv".format(checksum_z, file_number))



# slice and rewrite x
print("[INFO]  Slice and rewrite X");
count = 0
check_x = 0
with open("./data/xyz/" + file_number +  "x.csv", "r") as x_IN:
    for line in x_IN:
        if count == cut_number:
            x_OUT = open("./data/xyz_valid/" + file_new + "x.txt", "a")
            x_OUT.write(line)
            x_OUT.close()
            check_x += 1

        else:
            count += 1

# slice and rewrite y
print("[INFO]  Slice and rewrite Y");
count = 0
check_y = 0
with open("./data/xyz/" + file_number +  "y.csv", "r") as y_IN:
    for line in y_IN:
        if count == cut_number:
            y_OUT = open("./data/xyz_valid/" + file_new + "y.txt", "a")
            y_OUT.write(line)
            y_OUT.close()
            check_y += 1

        else:
            count += 1


# slice and rewrite z
print("[INFO]  Slice and rewrite Z");
count = 0
check_z = 0
with open("./data/xyz/" + file_number +  "z.csv", "r") as z_IN:
    for line in z_IN:
        if count == cut_number:
            z_OUT = open("./data/xyz_valid/" + file_new + "z.txt", "a")
            z_OUT.write(line)
            z_OUT.close()
            check_z += 1

        else:
            count += 1


# check written data
if (checksum_x - check_x) == cut_number:
	print("[CHECK] {} values from {}x.txt removed"
		.format(cut_number, file_number))
else:
	print("[CHECK][ERR] {} values from {}x.txt removed"
		.format(checksum_x - check_x, cutnumber))

if (checksum_y - check_y) == cut_number:
	print("[CHECK] {} values from {}y.txt removed"
		.format(cut_number, file_number))
else:
	print("[CHECK][ERR] {} values from {}y.txt removed"
		.format(checksum_y - check_y, cutnumber))

if (checksum_z - check_z) == cut_number:
	print("[CHECK] {} values from {}z.txt removed"
		.format(cut_number, file_number))
else:
	print("[CHECK][ERR] {} values from {}z.txt removed"
		.format(checksum_z - check_z, cutnumber))
