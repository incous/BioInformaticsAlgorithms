def protein_translation_problem(text):
	ret = ''
	for i in range(0, len(text), 3):
		ret += codon_table[text[i:i + 3]]
	return ret

f = open('RNA_codon_table_1.txt', 'r')
content = f.read()
codon_table = {}
for line in content.split('\n'):
	key = line.split(' ')[0]
	value = line.split(' ')[1]
	codon_table[key] = value
f.close()

f = open('protein_translation_problem.txt','r')
content = f.read()
lines = content.split('\n')
text = lines[0]
print protein_translation_problem(text)
f.close()