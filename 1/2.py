with open("1.txt", "r", encoding="UTF-8") as f:
	cal_file = f.readlines()

spelled_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

def find_digit(the_string):
	for i in range(len(the_string)):
		if the_string[i].isdigit():
			return (the_string[i], i)
	return ("nope", "nope")

def find_number_words(the_string):
	return_list = []
	for num in spelled_numbers:
		if num in the_string:
			str_index = the_string.find(num)
			return_list.append((num, str_index))
	return return_list
	

for line in cal_file:
	left_digit, left_index = find_digit(line)
	right_digit, right_index = find_digit(line[::-1])
	number_words = find_number_words(line)
	for words in number_words:
		try:
			if words[1] < left_index:
				left_digit = str(spelled_numbers.index(words[0]) + 1)
		except TypeError:
			left_digit = str(spelled_numbers.index(words[0]) + 1)
		try:
			if words[1] > len(line)-right_index:
				right_digit = str(spelled_numbers.index(words[0]) + 1)
		except TypeError:
			right_digit = str(spelled_numbers.index(words[0]) + 1)
	sum += int(left_digit + right_digit)

print(sum)
