idir = "input"

with open(idir, 'r') as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

print(grid)
ROWS = len(grid)
COLS = len(grid[0])
print(ROWS, COLS)

def find_next_position(curr_position, end_point):
	row = curr_position[0]
	col = curr_position[1]
	curr_value = grid[row][col]
	# print(curr_value)
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	if curr_value == '9':
		end_point.add(curr_position)
		return

	for d in directions:
		next_row = row + d[0]
		next_col = col + d[1]
		if 0 <= next_row < ROWS and 0 <= next_col < COLS:
			next_value = grid[next_row][next_col]
			if next_value == str(int(curr_value) + 1):
				# print(f"Next: ({next_row, next_col}), {next_value}")
				find_next_position((next_row, next_col), end_point)


def part1(grid):
	rows = len(grid)
	cols = len(grid[0])
	end_points = {}
	score = 0
	for row_idx in range(rows):
		for col_idx in range(cols):
			curr = grid[row_idx][col_idx]
			if curr == "0":
				end_point = set()
				find_next_position((row_idx, col_idx), end_point) 
				end_points[(row_idx, col_idx)] = end_point
				score += len(end_point)

	return end_points, score

end_points, score = part1(grid)

print(end_points)
print(score)
