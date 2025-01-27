import re
from fractions import Fraction
idir = 'input'


def find_combination(target_x, target_y, op_a, op_b):
	solutions = []
	x_a, y_a = op_a
	x_b, y_b = op_b
	max_a = target_x // x_a
	for count_a in range(max_a + 1):
		print(count_a)
		remaining_x = target_x - count_a * x_a
		remaining_y = target_y - count_a * y_a

		if remaining_x % x_b == 0 and remaining_y % y_b == 0:
			count_b = remaining_x // x_b
			if count_b >= 0 and count_b * y_b == remaining_y:
				solutions.append((count_a, count_b))


	return solutions


def get_cheapest_comb(solutions):
	lowest = float('inf')
	for ca, cb in solutions:
		lowest = min(lowest, ca * 3 + cb * 1)

	return lowest if lowest != float('inf') else 0


def find_combination_q2(target_x, target_y, op_a, op_b):
	target_x += 10000000000000
	target_y += 10000000000000
	solutions = []
	x_a, y_a = op_a # a c
	x_b, y_b = op_b # b d

	# this is Cramer's rule
	if x_a * y_b - y_a * x_b != 0:
		i = Fraction(y_b, x_a * y_b - x_b * y_a) * target_x + Fraction(-x_b, x_a * y_b - x_b * y_a) * target_y
		j = Fraction(-y_a, x_a * y_b - x_b * y_a) * target_x + Fraction(x_a, x_a * y_b - x_b * y_a) * target_y
		if i > 0 and j > 0 and i == int(i) and j == int(j):
			assert x_a * i + x_b * j == target_x
			assert y_a * i + y_b * j == target_y
			solutions.append((i, j))
	return solutions


# [((Ax, Ay), (Bx, By), (Px, Py))]

with open(idir, 'r') as f:
	idx = 1
	total = 0
	line = f.readline()

	while line:	
		if line == "\n":
			line = f.readline()
			continue

		matches = re.findall(r'\d+', line)
		numbers = list(map(int, matches))
		if idx % 3 == 1:
			# A
			op_a = numbers
		elif idx % 3 == 2:
			# B
			op_b = numbers
		else:
			target_x, target_y = numbers
			# print("*" * 10)

			# comb = find_combination(target_x, target_y, op_a, op_b)
			comb = find_combination_q2(target_x, target_y, op_a, op_b)			
			# print(comb)
			cheapest = get_cheapest_comb(comb)
			total += cheapest

		# input()
		idx += 1
		line = f.readline()

print(total)

