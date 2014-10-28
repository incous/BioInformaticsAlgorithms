def hamming_distance_problem(p, q):
	ret = 0
	for i in range(len(p)):
		if p[i] != q[i]: ret += 1
	return ret

def neighbors(pattern, distance):
	if 0 == distance:
		return [pattern]
	if 1 == len(pattern):
		return list('ACGT')
	neighborhood = []
	suffix_neighbors = neighbors(pattern[1:], distance)
	for item in suffix_neighbors:
		if hamming_distance_problem(item, pattern[1:]) < distance:
			for ch in list('ACGT'):
				neighborhood.append(ch + item)
		else:
			neighborhood.append(pattern[0] + item)
	return neighborhood

f = open('neighbors.txt','r')
content = f.read()
lines = content.split('\n')
pattern = lines[0]
distance = int(lines[1])
for item in neighbors(pattern, distance):
	print item
f.close()