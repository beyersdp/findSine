count = 0

with open ("4.txt", "r") as file:
	for line in file:
		count += 1

print(count)