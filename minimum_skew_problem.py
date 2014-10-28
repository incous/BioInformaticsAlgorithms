def minimum_skew_problem(genome):
	ret = [0]
	current = 0
	minnum = 0
	answer = []
	for i in genome:
		if 'C' == i: current -= 1
		elif 'G' == i: current += 1
		if current < minnum: minnum = current
		ret.append(current)
	for i in range(len(ret)):
		if ret[i] == minnum: answer.append(str(i))
	return ' '.join(answer)

f = open('minimum_skew_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
print minimum_skew_problem(text)