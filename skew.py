def skew(genome):
	ret = '0 '
	current = 0
	for i in genome:
		if 'C' == i: current -= 1
		elif 'G' == i: current += 1
		ret =+ str(current) + ' '
	return ret

f = open('skew.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
print skew(text)