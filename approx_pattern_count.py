def hamming_distance_problem(p, q):
	ret = 0
	for i in range(len(p)):
		if p[i] != q[i]: ret += 1
	return ret

def approx_pattern_count(text, pattern, distance):
	ret = 0
	for i in range(len(text) - len(pattern) + 1):
		if hamming_distance_problem(pattern, text[i:i + len(pattern)]) <= distance: ret += 1
	return ret

f = open('approx_pattern_count.txt','r')
content = f.read()
lines = content.split('\n')
pattern = lines[1]
text = lines[0]
distance = int(lines[2])
print approx_pattern_count(text, pattern, distance)