
def is_safe_values(num_a, num_b, decreasing):
	safe = True

	difference = num_a - num_b

	if abs(difference) <= 0 or abs(difference) > 3:
		#print(f"skipping row for diff of {difference}")
		safe = False

	if (difference < 0 and decreasing is True) or (difference > 0 and decreasing is not True):
		#print(f"skipping row because decrease/increase {difference} {decreasing}")
		safe = False
	
	return safe

def does_row_fail(row):
	decreasing = False

	if row[0] > row[1]:
		decreasing = True

	failed = False

	for i, num in enumerate(row[:-1]):
		#print(num)

		failed = not is_safe_values(num, row[i+1], decreasing)
		if failed:
			return failed
	return failed



def part1(rows):
	safe_count = 0

	for row in rows:
		row_fails = does_row_fail(row)

		if not row_fails:
			safe_count += 1

		print(row)
	print(f"final safe_count : {safe_count}")
	return



def part2(rows):
	safe_count = 0

	for row in rows:
		print("")
		print(row)
		row_fails = does_row_fail(row)

		if row_fails: 

			print(f"main row failed. Testing all sub rows")
			new_row_fails = True;

			for i in range(len(row)):
				new_row = row[0:i] + row[i+1:len(row)]

				print(f"Testing sub row {new_row}")

				new_row_fails = does_row_fail(new_row)

				if not new_row_fails:
					print(f"Row was successful with one missing entry")
					safe_count += 1
					break
			if new_row_fails:
				print(f"Row could not be saved")
		
		else:
			print(f"No failures!")
			safe_count += 1
		#_ = input("continue")

	print(f"final safe_count : {safe_count}")
	return



testInput = [
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9",
]

inputs = []

file_input = open("day_inputs/day2.txt", "r")

for line in file_input:

#for line in testInput:
	row = line.split(" ")
	inputs.append([int(num) for num in row])




print("part 1")
part1(inputs)
print("------------------\n\n\n\n")
_ = input("continue to part 2")
print("part 2")
part2(inputs)
