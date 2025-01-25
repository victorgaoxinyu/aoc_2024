"""
result = {
	<letter>: [
		()
	]
}
"""

def load_grid(filename):
	with open(filename, "r") as f:
		inputs = f.read().strip().splitlines()
		grid = [list(row) for row in inputs]
	return grid


# DFS??
def find_regions(grid):
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	rows, cols = len(grid), len(grid[0])
	visited = [[False for _ in range(cols)] for _ in range(rows)]
	region_stats = []

	def dfs(x, y, char):
		stack = [(x, y)]
		count = 0
		perimeter = 0

		while stack:
			cx, cy = stack.pop()
			count += 1
			for dx, dy in directions:
				nx, ny = cx + dx, cy + dy
				if 0 <= nx < rows and 0 <= ny < cols:
					if not visited[nx][ny] and grid[nx][ny] == char:
						visited[nx][ny] = True
						stack.append((nx, ny))
					elif grid[nx][ny] != char:
						perimeter += 1
				else:
					perimeter += 1
		return count, perimeter

	for i in range(rows):
		for j in range(cols):
			if not visited[i][j]:
				char = grid[i][j]
				visited[i][j] = True
				count, perimeter = dfs(i, j, char)
				region_stats.append((char, count, perimeter))

	return region_stats


def cal_price(region_stats):
	total = 0
	for _, c, p in region_stats:
		total += c * p

	return total


grid = load_grid("input")

region_stats = find_regions(grid)
print(region_stats)

total = cal_price(region_stats)
print(total)