idir = "input"

with open(idir, "r") as f:
	line = [int(i) for i in f.readline().split(" ")]



def blink_inplace(l):
	i = 0

	while i < len(l):
		length = len(str(l[i]))
		if l[i] == 0:
			l[i] = 1
			i += 1
		elif length % 2 == 0:
			half = length // 2
			left = int(str(l[i])[:half])
			right = int(str(l[i])[half:])

			l[i] = left
			l.insert(i + 1, right)

			i += 2
		else:
			l[i] *= 2024
			i += 1


def blink(l):
	new_list = []

	for i in l:
		if i == 0:
			new_list.append(1)
		elif len(str(i)) % 2 == 0:
			half = len(str(i)) // 2
			left = str(i)[:half]
			right = str(i)[half:]
			new_list.append(int(left))
			new_list.append(int(right))
		else:
			new_list.append(i * 2024)

	return new_list

print(line)

it = 0
iter_times = 75

while it < iter_times:
	print(it)
	blink_inplace(line)
	it += 1
print(len(line))