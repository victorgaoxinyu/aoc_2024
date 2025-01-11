from pprint import pprint
from tqdm import tqdm

idir = "input"

with open(idir, "r") as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

# find start point
rows = len(grid)
cols = len(grid[0])

found = False

for row in range(rows):
	for col in range(cols):
		curr = grid[row][col]
		if curr == "^":
			start = (row, col)
			found = True
			break
	if found:
		break

dir_idx = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def print_grid_with_marker(grid, markers, char):
	grid_with_markers = [list(row) for row in grid]
	for row, col in markers:
		grid_with_markers[row][col] = char


	for row in grid_with_markers:
		print("".join(row))


def simulate_guard(grid, start_pos, obstacle):
	visited = set()
	row, col = start_pos
	dir_idx = 0

	while (True):
		if (row, col, dir_idx) in visited:
			return True

		visited.add((row, col, dir_idx))
		next_r = row + directions[dir_idx][0]
		next_c = col + directions[dir_idx][1]

		if not (0 <= next_r < rows and 0 <= next_c < cols):
			return False

		if (next_r, next_c) == obstacle or grid[next_r][next_c] == "#":
			dir_idx = (dir_idx + 1) % 4
		else:
			row, col = next_r, next_c

def find_best_obstacle(grid, start_pos):

	cnt = 0

	candidate_positions = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "."]
	print(len(candidate_positions))

	for obs in tqdm(candidate_positions, total=len(candidate_positions)):
		valid = simulate_guard(grid, start_pos, obs)
		if valid:
			print(obs)
			cnt += 1
	return cnt

cnt = find_best_obstacle(grid, start)

print(cnt)