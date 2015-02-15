
# n = 15
# packages = (6, 9, 20)
packages = (10, 15, 19)
last_fail = 0
number_of_passes = 0
for n in range(1,200):
	passes = 0
	for a in range(0,n):
		for b in range (0,n):
			for c in range(0, n):
				if (packages[0]*a) + (packages[1]*b) + (packages[2]*c) == n:
					print 'for', n, 'nuggets get:', a, '* 6 packages,', b, '* 9 packages,', c, '* 20 Packages'
					passes = passes + 1

	if passes > 0:
		print n, 'Has some'
		number_of_passes = number_of_passes + 1
	else:
		print n, 'Has none'
		last_fail = n

	if n - last_fail == 6:
		print 'Given package sizes', packages[0], ',', packages[1], ',', 'and', packages[2], 'the largest number of McNuggets that cannot be bought in exact quantity is: ', last_fail
		break
