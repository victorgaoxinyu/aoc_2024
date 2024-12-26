# idir = "sample"
idir = "input"

with open(idir, "r") as f:
	inputs = f.read().strip().splitlines()
	grid = [list(row) for row in inputs]

# 	keyword = "XMAS"
# 	target_len = len(keyword)
# 	count = 0
# 	rows = len(grid)
# 	cols = len(grid[0])

# 	def is_valid_direction(row, col, dr, dc):
# 		for i in range(target_len):
# 			r = row + i * dr
# 			c = col + i * dc
# 			if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != keyword[i]:
# 				return False
# 		return True

# 	for row in range(rows):
# 		for col in range(cols):
# 			directions = [
# 			(0, 1),
# 			(0, -1),
# 			(1, 0),
# 			(-1, 0),
# 			(1, 1),
# 			(1, -1),
# 			(-1, 1),
# 			(-1, -1),
# 			]
# 			for dr, dc in directions:
# 				if is_valid_direction(row, col, dr, dc):
# 					count += 1
    
# print(count)

## part 2

print(grid)

"""
M.S
.A.
M.S
"""
count = 0
rows = len(grid)
cols = len(grid[0])
patterns = ["MAS", "SAM"]

def is_valid(x, y):
    for top_mas in patterns:
        for bottom_mas in patterns:
            if (
                grid[x][y] == top_mas[0]
                and grid[x + 2][y + 2] == top_mas[2]
                and grid[x + 1][y + 1] == "A"
                and grid[x + 2][y] == bottom_mas[0]
                and grid[x][y + 2] == bottom_mas[2]
            ):
                print(f"Pattern matched at ({x}, {y}) with top {top_mas} and bottom {bottom_mas}")
                return True
            else:
                print("*"* 20)
                print(f"{grid[x][y]}| |{grid[x][y + 2]}")
                print(f" |{grid[x + 1][y + 1]}| ")
                print(f"{grid[x + 2][y]}| |{grid[x + 2][y + 2]}")

    return False


for i in range(rows - 2):
	for j in range(cols - 2):
		if grid[i + 1][j + 1] == "A" and is_valid(i, j):
			count += 1

print(count)