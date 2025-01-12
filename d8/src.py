from pprint import pprint
import itertools

idir = "input"

with open(idir, "r") as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

ROWS = len(grid)
COLS = len(grid[0])

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

res = find_antenna(grid)
pprint(res)

antinode_res = {}
uniq_res = set()

for type, antennas in res.items():
	antinode_res[type] = []
	combinations = list(itertools.combinations(antennas, 2))
	for comb in combinations:
		ant1, ant2 = get_antinodes(comb[0], comb[1])
		if valid_antinodes(ant1):
			antinode_res[type].append(ant1)
			uniq_res.add(ant1)

		if valid_antinodes(ant2):
			antinode_res[type].append(ant2)
			uniq_res.add(ant2)

pprint(antinode_res)
print(uniq_res)
print(len(uniq_res))
# ant1, ant2 = get_antinodes((2, 5), (3, 7))
# print(ant1, ant2)