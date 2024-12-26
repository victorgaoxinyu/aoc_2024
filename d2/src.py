# idir = 'sample'
idir = "input"


def is_safe(items):
	prev_delta = 0

	for idx in range(1, len(items)):
		prev_num = items[idx - 1]
		curr_num = items[idx]

		delta = curr_num - prev_num

		if abs(delta) < 1 or abs(delta) > 3:
			return False

		if delta * prev_delta < 0:
			return False

		prev_delta = delta

	return True


with open(idir, 'r') as f:
	line = f.readline()
	count = 0

	while line:

		items = [int(i) for i in line.strip().split(" ")]

		safe = is_safe(items)

		if not safe:
			for idx in range(len(items)):
				safe = is_safe([x for i, x in enumerate(items) if i != idx])
				if safe:
					break

		if safe:
			count += 1

		line = f.readline()

print(count)