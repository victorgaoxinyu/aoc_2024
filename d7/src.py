from itertools import product
idir = "input"

def generate_possible_combinations_q2(numbers):
	operators = ['+', '*', '||']
	n = len(numbers) - 1
	result = set()

	for ops in product(operators, repeat=n):
		expression = [str(numbers[0])]
		for num, op in zip(numbers[1:], ops):
			expression.append(op)
			expression.append(str(num))

		yield expression	


def generate_possible_combinations(numbers):
	operators = ['+', '*']
	n = len(numbers) - 1
	result = set()

	for ops in product(operators, repeat=n):
		expression = [str(numbers[0])]
		for num, op in zip(numbers[1:], ops):
			expression.append(op)
			expression.append(str(num))

		yield expression


def eval_result_q2(expression):
	total = int(expression[0])
	for i in range(1, len(expression), 2):
		op = expression[i]
		num = int(expression[i + 1])
		if op == "+":
			total += num
		elif op == "*":
			total *= num
		elif op == "||":
			total = int(str(total) + str(num))

	return total


def eval_result(expression):
	total = int(expression[0])
	for i in range(1, len(expression), 2):
		op = expression[i]
		num = int(expression[i + 1])
		if op == "+":
			total += num
		elif op == "*":
			total *= num
	return total


with open(idir, "r") as f:
	total = 0
	cnt = 1
	line = f.readline().strip()

	while line:
		print(f"Checking line: {cnt}")
		exp = int(line.split(":")[0])
		nums = [int(i) for i in line.split(":")[1].strip().split(" ")]
		# for i in generate_possible_combinations(nums):
		# 	res = eval_result(i)
		# 	if res == exp:
		# 		total += res
		# 		break

		for i in generate_possible_combinations_q2(nums):
			res = eval_result_q2(i)
			if res == exp:
				total += res
				break

		line = f.readline().strip()
		cnt += 1

print(total)