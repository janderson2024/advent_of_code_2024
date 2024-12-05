def print_formated(input_mat):
	for line in input_mat:
		print(line)


def follows_rules(rules, page):
	failed = False
	for rule in rules:
		if page.count(rule[0]) and page.count(rule[1]):
			index = page.index(rule[0])

			#print(page[index+1:])
			#print(page[index+1:].count(rule[1]))


			if page[index+1:].count(rule[1]) == 0:
				#not a valid page
				failed = True
				#print(f"page failed")
				break

	return not failed



def part1(rules, pages):

	#print_formated(rules)
	#print_formated(pages)


	total = 0
	for page in pages:
		print(f"checking page: {page}")

		
		if follows_rules(rules, page):
			#print(f"page passed!")
			total += page[len(page)//2]

	print(f"total sum : {total}")
	return



def part2(rules, pages):

	failed_pages = []

	total = 0

	for page in pages:
		if not follows_rules(rules, page):
			failed_pages.append(page)

	print_formated(failed_pages)

	for page in failed_pages:

		while not follows_rules(rules, page):

			for rule in rules:
				if page.count(rule[0]) and page.count(rule[1]):
					index = page.index(rule[0])

				#print(page[index+1:])
				#print(page[index+1:].count(rule[1]))


					if page[index+1:].count(rule[1]) == 0:
						scnd_indx = page.index(rule[1])

						page[scnd_indx] = rule[0]
						page[index] = rule[1]

						print(f"new page: {page}")
						break 
		
		print(f"fixed page order for page: {page}")

		total += page[len(page)//2]
		print(f"New fixed sum: {total}")
	return



testInput = [
	"47|53",
	"97|13",
	"97|61",
	"97|47",
	"75|29",
	"61|13",
	"75|53",
	"29|13",
	"97|29",
	"53|29",
	"61|53",
	"97|53",
	"61|29",
	"47|13",
	"75|47",
	"97|75",
	"47|61",
	"75|61",
	"47|29",
	"75|13",
	"53|13",
	"\n",
	"75,47,61,53,29",
	"97,61,53,29,13",
	"75,29,13",
	"75,97,47,61,53",
	"61,13,29",
	"97,13,75,29,47",
]

rules = []
pages = []
swtich = False

file_input = open("day_inputs/day5.txt", "r")

for line in file_input:

#for line in testInput:
	if line == "\n":
		swtich = True
		continue
	if not swtich:
		rules.append(line)
	else:
		pages.append([int(page) for page in line.split(",")])



rules = [(int(x[0]),int(x[1])) for x in [rule.split("|") for rule in rules]]


print("part 1")
part1(rules, pages)
print("------------------\n\n\n\n")
_ = input("continue to part 2")
print("part 2")
part2(rules, pages)