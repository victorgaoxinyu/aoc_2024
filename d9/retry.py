idir = "input"

with open(idir, 'r') as f:
	m = f.readline().strip()


def pprint(m):
	print("".join([str(i) for i in m]))


def part2(m):
	A = []
	FINAL = []
	SPACE = []
	pos = 0
	file_id = 0

	for i, c in enumerate(m):
		if i%2 == 0:
			A.append((pos, int(c), file_id))

			for i in range(int(c)):
				FINAL.append(file_id)
				pos += 1

			file_id += 1
		else:
			SPACE.append((pos, int(c)))
			for i in range(int(c)):
				FINAL.append(".")
				pos += 1

	# pprint(FINAL)

	for (pos, sz, file_id) in reversed(A):
		for space_i, (space_pos, space_sz) in enumerate(SPACE):
			if space_pos < pos and sz <= space_sz:
				for i in range(sz):
					FINAL[pos+i] = "."
					FINAL[space_pos+i] = file_id
				SPACE[space_i] = (space_pos + sz, space_sz-sz)
				break

	# pprint(FINAL)

	total = 0
	for i, c in enumerate(FINAL):
		if c != ".":
			total += i * c

	return total


total = part2(m)
print(total)