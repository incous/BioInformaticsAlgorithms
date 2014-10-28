def frequent_words_problem(text, wordlen):
	ret = {}
	for i in range(len(text) - wordlen + 1):
		key = text[i:i+wordlen]
		if ret.has_key(key): ret[key] += 1
		else: ret[key] = 1
	maxnum = sorted(ret.values())[-1]
	answer = []
	for item in ret:
		if maxnum == ret[item]:	answer.append(item)
	return ' '.join(answer)

f = open('frequent_words_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
wordlen = int(lines[1])
print frequent_words_problem(text, wordlen)