def hamming_distance_problem(p, q):
	ret = 0
	for i in range(len(p)):
		if p[i] != q[i]: ret += 1
	return ret

f = open('hamming_distance_problem.txt','r')
content = f.read()
lines = content.split('\n')
p = lines[0]
q = lines[1]
print hamming_distance_problem(p, q)