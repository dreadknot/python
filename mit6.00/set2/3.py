
# n = 15

last_fail = 0
number_of_passes = 0
for n in range(1,56):
	passes = 0
	for a in range(0,n):
		for b in range (0,n):
			for c in range(0, n):
				if (6*a) + (9*b) + (20*c) == n:
					print 'for', n, 'nuggets get:', a, '* 6 packages,', b, '* 9 packages,', c, '* 20 Packages'
					passes = passes + 1

	if passes > 0:
		print n, 'Has some'
		number_of_passes = number_of_passes + 1
	else:
		print n, 'Has none'
		last_fail = n

	if n - last_fail == 6:
		print 'Largest number of McNuggets that cannot be bought in exact quantity: ', last_fail
		break
