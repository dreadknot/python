
with open('Homo_sapiens.GRCh38.dna.chromosome.1.fa', 'r') as f:
	for line in f:
		# print line.rstrip()
		for char in line.rstrip():
			if char == 'A':
			    print "01\n"
			elif char == 'G':
			    print "10\n"
			elif char == 'C':
			    print "11\n"
			elif  char == 'T':
			    print "00\n"
