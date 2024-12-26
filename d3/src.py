import re


# idir = "sample"
idir = "input"

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
flag_pattern = r"do\(\)|don't\(\)"

combined_pattern = rf"{pattern}|{flag_pattern}"

sum = 0
enabled = True

with open(idir, "r") as f:
	line = f.readline()

	while line:
		# print(line)
		for match in re.finditer(combined_pattern, line):
			if match.group(1) and match.group(2):
				if enabled:
					x = int(match.group(1))
					y = int(match.group(2))
					sum += x * y
			elif match.group(0) == "do()":
				enabled = True
			elif match.group(0) == "don't()":
				enabled = False

		line = f.readline()

print(sum)