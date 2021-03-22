def solution(program, flag_rules, commands):
	answer = []
	new_flag = dict()
	new_command = []
	for flag in flag_rules:
		flag = list(flag.split())
		new_flag[flag[0]] = flag[1]

	for command in commands:
		new_command.append(list(command.split()))

	print(new_flag)
	print(new_command)
	ans = []
	for command in new_command:
		if command.pop(0) != program:
			answer.append(False)
			break
		temp = []
		for c in command:
			print(c)


print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))
print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))
a = 'NULL'
