from pprint import pprint

# idir = "sample"
idir = "input"

global_map = dict()


def update_map(line, global_map):
	splits = line.strip().split("|")
	first_number = splits[0]
	secon_number = splits[1]

	if first_number not in global_map:
		global_map[first_number] = {secon_number: 'after'}
	else:
		global_map[first_number].update({secon_number: 'after'})

	if secon_number not in global_map:
		global_map[secon_number] = {first_number: 'before'}
	else:
		global_map[secon_number].update({first_number: 'before'})


def check_is_valid(line, global_map):
	items = [i for i in line.strip().split(",")]
	length = len(items)
	for idx in range(length - 1):
		curr_n = items[idx]
		next_n = items[idx + 1]
		# print("curr", curr_n)
		# print("next", next_n)

		# print(global_map[curr_n])

		if global_map[curr_n][next_n] != 'after':
			return 0
    
	return int(items[int((length - 1) / 2)])

sum = 0

with open(idir, "r") as f:
	line = f.readline()

	while line:
		if "|" in line:
			update_map(line, global_map)

		if "," in line:
			sum += check_is_valid(line, global_map)

		line = f.readline()

print(sum)