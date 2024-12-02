def part1(left_side, right_side):
	left_side.sort()
	right_side.sort()

	print(left_side)
	print(right_side)

	differences = [abs(x-y) for x,y in list(zip(left_side, right_side))]

	print(differences)


	print(f'Result = {sum(differences)}')



def part2(left_side, right_side):
	similarity_score = 0

	for number in left_side:
		number_sim_score = number *right_side.count(number)
		print(f"({number} : {number_sim_score} )")
		similarity_score += number_sim_score

	print(f"similarity_score is {similarity_score}")



testInput = [
"3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3",
]

left_side = []

right_side = []

input = open("day_inputs/day1.txt", "r")

for line in input:

#for line in testInput:
	left, right = line.split("   ")
	left_side.append(int(left))
	right_side.append(int(right))


print("part 1")
part1(left_side, right_side)
print("------------------\n\n\n\n")
print("part 2")
part2(left_side, right_side)