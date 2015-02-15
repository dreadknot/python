
# n = 15


for n in range(1,50):
	passes = 0
	last = 0
	for a in range(0,n):
		for b in range (0,n):
			for c in range(0, n):
				if (6*a) + (9*b) + (20*c) == n:
					print 'for', n, 'nuggets get:', a, '* 6 packages,', b, '* 9 packages,', c, '* 20 Packages'
					passes = passes + 1
				else:
					last = n
	if passes == 0:
		print n, 'has none'
		# print 'Largest number of McNuggets that cannot be bought in exact quantity: ', n


