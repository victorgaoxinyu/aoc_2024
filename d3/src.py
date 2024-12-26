import re


# idir = "sample"
idir = "input"

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
sum = 0

with open(idir, "r") as f:
	line = f.readline()

	while line:
		matches = re.findall(pattern, line)

		for x, y in matches:
			sum += int(x) * int(y)

		line = f.readline()

print(sum)