import itertools

def reverse_complement_problem(text):
	ret = ''
	for i in range(len(text)):
		if 'A' == text[len(text) - i - 1]: ret += 'T'
		elif 'T' == text[len(text) - i - 1]: ret += 'A'
		elif 'C' == text[len(text) - i - 1]: ret += 'G'
		elif 'G' == text[len(text) - i - 1]: ret += 'C'
	return ret

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
	return neighborhood

def frequent_words_mismatch(text, kmer, distance):
	target = []
	for i in range(len(text) - kmer + 1):
		pattern = text[i:i + kmer]
		target.extend(neighbors(pattern, distance))
	target = list(set(target))
	maxnum = 0
	ret = []
	for pattern in target:
		number = approx_pattern_matching_count(text, pattern, distance) + approx_pattern_matching_count(text, reverse_complement_problem(pattern), distance)
		if number == maxnum:
			ret.append(pattern)
		elif number > maxnum:
			maxnum = number
			ret = [pattern]
	return ' '.join(list(set(ret)))

f = open('frequent_words_mismatch_includes_reverse.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
params = lines[1].split(' ')
kmer = int(params[0])
distance = int(params[1])
print frequent_words_mismatch(text, kmer, distance)
f.close()