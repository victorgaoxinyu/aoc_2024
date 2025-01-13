idir = "sample"

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


def move_whole_file(m):
	ptr_l = 0
	ptr_r = len(m) - 1

	candidate_file = []
	candidate_empty = []

	while ptr_r > ptr_l:

		if m[ptr_l] != ".":
			if candidate_empty == []:
				ptr_l += 1
				continue
			else:
				print("*"*20)
				print(ptr_l, candidate_empty, candidate_file)
				pass
		else:
			candidate_empty.append(".")
			ptr_l += 1
			continue

		if m[ptr_r] == ".":
			if candidate_file == []:
				ptr_r -= 1
				continue
			else:
				if len(candidate_file) <= len(candidate_empty):
					print("Trying replace: ", candidate_empty, candidate_file)
					start_idx = ptr_l - len(candidate_empty)
					end_idx = start_idx + len(candidate_file)
					m[start_idx: end_idx] = candidate_file
					ptr_l = end_idx + 1

					start_idx = ptr_r
					end_idx = ptr_r + len(candidate_file)
					m[start_idx: end_idx] = "."
					ptr_r -= 1

					# pprint_m(m)
					continue
				else:
					candidate_file = []
					ptr_r -=1
					continue
		else:
			if candidate_file == []:
				candidate_file.append(m[ptr_r])
				ptr_r -= 1
				continue
			else:
				if m[ptr_r] == candidate_file[0]:
					candidate_file.append(m[ptr_r])
					ptr_r -= 1
				else:
					if len(candidate_file) <= len(candidate_empty):
						start_idx = ptr_l - len(candidate_empty)
						end_idx = start_idx + len(candidate_file)
						m[start_idx: end_idx] = candidate_file
						ptr_l = end_idx + 1

						start_idx = ptr_r
						end_idx = ptr_r + len(candidate_file)
						m[start_idx: end_idx] = "."
						ptr_r -= 1
						# pprint_m(m)

						continue
					else:
						candidate_file = [m[ptr_r]]
						ptr_r -= 1
						continue




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

after_move = move_whole_file(res)

# q1
# after_move = move_file_blocks(res)
# checksum = cal_checksum(after_move)
# print(checksum)