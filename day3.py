import re


def parse_mul(inp):
	split_res = inp.split(",")
	num1 = int(split_res[0][4:])
	num2 = int(split_res[1][0:len(split_res[1])-1])
	print(f"{num1} *** {num2}")

	return (num1 * num2)



def part1(rows):
	regex_check = "(mul\([0-9]{1,3},[0-9]{1,3}\))"


	sum = 0
	for row in rows:
		print(row)
		section_sum = 0
		results = re.findall(regex_check, row)

		for result in results:
		
			section_sum += parse_mul(result)

		print(f"Section sum = {section_sum}")
		sum += section_sum


	print(f"final sum: {sum}")
	return



def part2(rows):
	regex_check = "(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\))"

	sum = 0
	#section_sum = 0
	for row in rows:
		print(row)
		section_sum = 0

		results = re.findall(regex_check, row)

		enabled = True
		for result in results:

			result = list(filter(None, result))[0]

			print(result)
			if result[0] == "m":
				if enabled:
					section_sum += parse_mul(result)
				else:
					print("   - skipping")
			elif result == "do()":
				print("   - enable")
				enabled = True
			elif result == "don't()":
				print("   - disable")
				enabled = False
			else:
				_ = input("WEE WOOO")

		print(f"Section sum = {section_sum}")
		sum += section_sum
		_ = input("continue to part 2")
	print(f"final sum: {sum}")
	return



testInput = [
	"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
	"xmul(200,433)%&mul[3,7]!@^do_not_mul(5,5)+mul(3233,64]then(mul(11,8)mul(8,5))",
	"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
	"xmul(0,4)&mul[3,7]!^don't()_mul(54,5)+mul(32,64](mul(11,8)undo()?mul(80,5))",
]

inputs = []

file_input = open("day_inputs/day3.txt", "r")

for line in file_input:

#for line in testInput:
	inputs.append(line)




print("part 1")
part1(inputs)
print("------------------\n\n\n\n")
#_ = input("continue to part 2")
print("part 2")
part2(inputs)