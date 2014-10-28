def pattern_count(text, pattern):
	ret = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern: ret += 1
	return ret

f = open('pattern_count.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
pattern = lines[1]
print patterncount(text, pattern)