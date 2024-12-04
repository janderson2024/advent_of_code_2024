def buffer_padding(input_mat):
	line_len = len(input_mat[0])


	input_mat.insert(0, ["."]*line_len)
	input_mat.append(["."]*line_len)

	for line in input_mat:
		line.insert(0, ".")
		line.append(".")


	return input_mat

def un_padding(input_mat):
	input_mat.pop(0)
	input_mat.pop(len(input_mat)-1)

	line_len = len(input_mat[0])

	for line in input_mat:
		line.pop(0)
		line.pop(line_len-2)

	return input_mat

def print_formated(input_mat):
	for line in input_mat:
		print(line)


full_dirs=[[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

def add_next_letter_to_search_list(matrix, x, y, next_letter, directions=full_dirs):
	search_list = []
	for dirr in directions:
		check_letter = matrix[x+dirr[0]][y+dirr[1]]

		if check_letter == next_letter:
			search_list.append((x+dirr[0], y+dirr[1], dirr))
		print(check_letter)
	return search_list




def part1(rows):
	fr = buffer_padding(rows)
	print_formated(fr)

	x_search_list = []
	m_search_list = []
	a_search_list = []


	for i, row in enumerate(fr):
		for j, letter in enumerate(row):
			if letter == ".":
				continue
			if letter != "X":
				continue

			x_search_list = add_next_letter_to_search_list(fr, i, j, "M")

	print(x_search_list)
	print_formated(fr)
	print("Finished running the X list. Trying M...")

	for entry in x_search_list:
		print(entry[0], entry[1], entry[2][1])
		m_search_list = add_next_letter_to_search_list(fr, entry[0], entry[1], "A", directions=[entry[2]])


	print(m_search_list)
	print_formated(fr)
	print("Finished running the M list. Trying A...")

	for entry in m_search_list:
		print(entry[0], entry[1], entry[2][1])
		a_search_list = add_next_letter_to_search_list(fr, entry[0], entry[1], "S", directions=[entry[2]])
	
	print(a_search_list)
	print_formated(fr)
	print(f"Finished running the A list....")

	print(f"The total is : {len(a_search_list)}")




	return



def part2(rows):

	fr = buffer_padding(rows)
	print_formated(fr)

	total = 0

	for i, row in enumerate(fr):
		for j, letter in enumerate(row):
			if letter == ".":
				continue
			if letter != "A":
				continue

			left_word = fr[i-1][j-1] + fr[i][j] + fr[i+1][j+1]
			right_word = fr[i-1][j+1] + fr[i][j] + fr[i+1][j-1]

			if [left_word, right_word, left_word[::-1], right_word[::-1]].count("MAS") == 2:
				total += 1


	print(f'Total X-MAS is : {total}')

	return



testInput = [
	"MMMSXXMASM",
	"MSAMXMSMSA",
	"AMXSXMAAMM",
	"MSAMASMSMX",
	"XMASAMXAMM",
	"XXAMMXXAMA",
	"SMSMSASXSS",
	"SAXAMASAAA",
	"MAMMMXMMMM",
	"MXMXAXMASX"
]

inputs = []

file_input = open("day_inputs/day4.txt", "r")

for line in file_input:

#for line in testInput:
	inputs.append(list(line))




print("part 1")
part1(inputs)
print("------------------\n\n\n\n")
_ = input("continue to part 2")
print("part 2")
part2(inputs)