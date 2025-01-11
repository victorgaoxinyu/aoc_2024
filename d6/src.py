# idir = "sample"
idir = "input"

with open(idir, "r") as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

# from pprint import pprint
# pprint(grid)


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


# grid traverse
dir_idx = 0
row, col = start
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
uniq_steps = {(row, col)}

"""
^ > v <: (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)

"""

while 0 < row < rows and 0 < col < cols:

	# check next element
	next_r, next_c = row + directions[dir_idx][0], col + directions[dir_idx][1]

	if not (0 <= next_r < rows) and (0 <= next_c < cols):
		print(next_r, next_r)
		break

	next = grid[next_r][next_c]
	if next == "#":
		print(f"Blcoked at {next_r, next_c}")
		print(f"Curr direction: {dir_idx}")
		dir_idx = (dir_idx + 1) % 4
		print(f"New direction: {dir_idx}")

	else:
		print(grid[row][col])
		uniq_steps.add((row, col))
		row, col = next_r, next_c


print(len(uniq_steps) + 1)
