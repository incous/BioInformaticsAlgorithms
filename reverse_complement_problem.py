def reverse_complement_problem(text):
	ret = ''
	for i in range(len(text)):
		if 'A' == text[len(text) - i - 1]: ret += 'T'
		elif 'T' == text[len(text) - i - 1]: ret += 'A'
		elif 'C' == text[len(text) - i - 1]: ret += 'G'
		elif 'G' == text[len(text) - i - 1]: ret += 'C'
	return ret

f = open('reverse_complement_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
print reverse_complement_problem(text)