idir = "input"

with open(idir, 'r') as f:
	m = f.readline().strip()

# m = '12345'


def pprint_m(m):
	print("".join(m))

def expand_map(m):
	res = []
	for idx, m_idx in enumerate(range(0, len(m), 2)):
		block_of_file = int(m[m_idx])
		res.extend([str(idx)] * block_of_file)

		if m_idx + 1 < len(m):
			block_of_free = int(m[m_idx + 1])
			res.extend(["."] * block_of_free)
		else:
			break

	return res


def move_file_blocks(m):
	ptr_l = 0
	ptr_r = len(m) - 1

	while ptr_r > ptr_l:

		if m[ptr_r] == ".":
			ptr_r -= 1
			continue

		if m[ptr_l] != ".":
			ptr_l += 1
			continue
		else:
			m[ptr_l] = m[ptr_r]
			m[ptr_r] = "."
			# pprint_m(m)

	return m


def cal_checksum(m):
	total = 0
	for idx in range(len(m)):
		if m[idx] == ".":
			break
		total += idx * int(m[idx])

	return total

print(m, type(m))

res = expand_map(m)

pprint_m(res)

after_move = move_file_blocks(res)

checksum = cal_checksum(after_move)

print(checksum)