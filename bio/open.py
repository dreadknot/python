
import base64

with open('Homo_sapiens.GRCh38.dna.chromosome.1.fa', 'r') as f:
	for line in f:
		# print line.rstrip()
		byte = ''
		for char in line.rstrip():
			if char == 'A':
			    # print "01\n"
			    byte = byte + '01'
			elif char == 'G':
			    # print "10\n"
			    byte = byte + '10'
			elif char == 'C':
			    # print "11\n"
			    byte + byte + '11'
			elif  char == 'T':
			    # print "00\n"
			    byte = byte + '00'
		if len(byte) >= 32:
			print byte

