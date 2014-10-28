def pattern_matching_problem(pattern, genome):
	ret = []
	for i in range(len(genome) - len(pattern)):
		if pattern == genome[i:i + len(pattern)]: ret.append(str(i))
	return ' '.join(ret)

f = open('pattern_matching_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[1]
pattern = lines[0]
print pattern_matching_problem(pattern, text)