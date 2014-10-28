import itertools, time
from multiprocessing import Process
cores = 8

def hamming_distance_problem(p, q):
	ret = 0
	for i in range(len(p)):
		if p[i] != q[i]: ret += 1
	return ret

def approx_pattern_matching_count(text, pattern, distance):
	ret = 0
	for i in range(len(text) - len(pattern) + 1):
		if hamming_distance_problem(pattern, text[i:i + len(pattern)]) <= distance: ret += 1
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
	return list(set(neighborhood))

def y(text, patterns, distance):
	ret = [0]
	for pattern in patterns:
		number = approx_pattern_matching_count(text, pattern, distance)
		if number == ret[0]:
			ret.append(pattern)
		elif number > ret[0]:
			ret[0:2] = [number,pattern]
			ret[2:] = []
	print ret[0], ' '.join(ret[1:])
	
f = open('frequent_words_mismatch.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
params = lines[1].split(' ')
kmer = int(params[0])
distance = int(params[1])
fullset = []
#for item in itertools.product('ACGT', repeat = kmer):
#	fullset.append(''.join(item))
for i in range(len(text) - kmer + 1):
	fullset.extend(neighbors(text[i:i + kmer], distance))
fullset = list(set(fullset))
wholerange = [fullset[i::cores] for i in range(cores)]
for core in range(cores):
	if __name__ == '__main__':
	    p = Process(target=y, args=(text, wholerange[core], distance,))
	    p.start()
f.close()
