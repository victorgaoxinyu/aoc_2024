from pprint import pprint
import itertools

idir = "input"

with open(idir, "r") as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

ROWS = len(grid)
COLS = len(grid[0])
print(ROWS, COLS)


def print_grid_with_marker(grid, markers, char):
	grid_with_markers = [list(row) for row in grid]
	for row, col in markers:
		grid_with_markers[row][col] = char


	for row in grid_with_markers:
		print("".join(row))


def find_antenna(grid):
	rows = len(grid)
	cols = len(grid[0])
	result_dict = {}

	for r_idx in range(rows):
		for c_idx in range(cols):
			loc = (r_idx, c_idx)
			content = grid[r_idx][c_idx]
			if content != ".":
				if content in result_dict:
					result_dict[content].add(loc)
				else:
					result_dict[content] = {loc}

	return result_dict


def valid_antinodes(ant):
	if not (0 <= ant[0] < ROWS and 0 <= ant[1] < COLS):
		return False

	return True


def get_antinodes(a1, a2):
	w_diff = a2[1] - a1[1]
	h_diff = a2[0] - a1[0]

	ant1 = (a1[0] - h_diff, a1[1] - w_diff)
	ant2 = (a2[0] + h_diff, a2[1] + w_diff)

	return ant1, ant2

def get_valid_antinodes_q2(a1, a2):
	uniq_res = set()
	w_diff = a2[1] - a1[1]
	h_diff = a2[0] - a1[0]

	n = 1
	while True:
		ant_left = (a1[0] - h_diff * n, a1[1] - w_diff * n)
		if valid_antinodes(ant_left):
			uniq_res.add(ant_left)
			n += 1
		else:
			n = 1
			break

	while True:
		ant_right = (a2[0] + h_diff * n, a2[1] + w_diff * n)
		if valid_antinodes(ant_right):
			uniq_res.add(ant_right)
			n += 1
		else:
			break

	return uniq_res


res = find_antenna(grid)

antinode_res = {}
uniq_res = set()

# for type, antennas in res.items():
# 	antinode_res[type] = []
# 	combinations = list(itertools.combinations(antennas, 2))
# 	for comb in combinations:
# 		ant1, ant2 = get_antinodes(comb[0], comb[1])
# 		if valid_antinodes(ant1):
# 			antinode_res[type].append(ant1)
# 			uniq_res.add(ant1)

# 		if valid_antinodes(ant2):
# 			antinode_res[type].append(ant2)
# 			uniq_res.add(ant2)

# pprint(antinode_res)
# print(uniq_res)
# print(len(uniq_res))

cnt = 0
for type, antennas in res.items():
	combinations = list(itertools.combinations(antennas, 2))
	for comb in combinations:
		tmp_res = get_valid_antinodes_q2(comb[0], comb[1])
		cnt += len(tmp_res)
		uniq_res = uniq_res | tmp_res | antennas  # include antennas!

print(uniq_res)
print(len(uniq_res))

# print_grid_with_marker(grid, uniq_res, "#")

