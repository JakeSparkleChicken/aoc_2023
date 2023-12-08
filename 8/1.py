moves = "LRLRRLRLRLLRRRLLLRLLRRLLRRRLRLRLRRRLRRLRLRRRLRRRLRRRLRRRLRRLRRRLRRRLRRLLLRLLRLRRRLRRRLRRLRLRLRLRRRLRRRLRRRLRRLRRLRRLLRRLRRRLLRRLRRRLRRRLRRRLRLRRLRLRRRLRRLLRLRLLRLRLRRRLRLRRLLRRRLRLRLRLRLRLRRLRLRRLLLLRRLRRLRRRLRRLRRLRRRLRRLRRRLLRLRRLLRLRRLRRLRRLLRRRLRLRLRRRLRRLRLLRLRRRR"

with open("1.txt", "r", encoding="UTF-8") as f:
	orig_list = f.readlines()

map_dict = {}

for line in orig_list:
	line_parts = line.strip().split("=")
	parts = line_parts[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
	map_dict[line_parts[0].strip()] = (parts[0], parts[1])

def make_move(position, direction):
	if direction == "L":
		return map_dict[position][0]
	return map_dict[position][1]

position = "AAA"
steps = 0

def step_through_moves(steps, position, moves):
	for move in moves:
		position = make_move(position, move)
		steps += 1
		if position == "ZZZ":
			return str(steps) + " " + (position)
		if steps > len(moves) - 1:
			new_moves = moves + moves
			return_answer = step_through_moves(steps, position, new_moves)
			return return_answer

print(step_through_moves(steps, position, moves))
