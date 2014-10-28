def pattern_count(text, pattern):
	ret = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern: ret += 1
	return ret

def clump_finding_problem(text, wordlen, textlen, minoccu):
	ret = []
	for i in range(len(text) - wordlen):
		pattern = text[i:i + wordlen]
		if pattern in ret: continue
		elif pattern_count(text[i:i + textlen], pattern) >= minoccu: ret.append(pattern)
	return ' '.join(ret)

f = open('clump_finding_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
params = lines[1].split(' ')
wordlen = int(params[0])
textlen = int(params[1])
minoccu = int(params[2])
print clump_finding_problem(text, wordlen, textlen, minoccu)