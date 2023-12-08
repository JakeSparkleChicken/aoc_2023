with open("1.txt", "r", encoding="UTF-8") as f:
	cal_file = f.readlines()

sum = 0

def find_digit(the_string):
	for i in range(len(the_string)):
		if the_string[i].isdigit():
			return the_string[i]

for line in cal_file:
	left_digit = find_digit(line)
	right_digit = find_digit(line[::-1])
	sum += int(left_digit + right_digit)

print(sum)
