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

def simulate_guard(grid, start_pos, obstacle=None):
	row, col = start_pos
	state_history = set()
	visited = set()
	dir_idx = 0
	steps = 0
	max_steps = 10000
	valid = True

	while (row, col, dir_idx) not in state_history and steps < max_steps:
		state_history.add((row, col, dir_idx))
		visited.add((row, col))
		next_r = row + directions[dir_idx][0]
		next_c = col + directions[dir_idx][1]

		# print(f"Curr: {row, col, dir_idx}, Next: {next_r, next_c}")

		if not (0 <= next_r < rows and 0 <= next_c < cols):
			valid = False
			break

		if (next_r, next_c) == obstacle or grid[next_r][next_c] == "#":
			dir_idx = (dir_idx + 1) % 4
		else:
			row, col = next_r, next_c

		steps += 1

	return visited, valid

def find_best_obstacle(grid, start_pos):

	visited, _ = simulate_guard(grid, start_pos)
	print(f"Origin: {len(visited)}")

	# print_grid_with_marker(grid, visited, "X")

	best_obstacle = None
	max_visited = len(visited)
	cnt = 0

	candidate_positions = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "."]
	print(len(candidate_positions))
	# print_grid_with_marker(grid, candidate_positions, "O")

	for obs in tqdm(candidate_positions, total=len(candidate_positions)):
		visited, valid = simulate_guard(grid, start_pos, obs)
		if len(visited) < max_visited and valid:
			print(obs, valid)
			# print_grid_with_marker(grid, visited, "X")
			print("<" * 20)
			cnt += 1
	return cnt

cnt = find_best_obstacle(grid, start)

print(cnt)