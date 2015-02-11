primes = [2]
# go through all the odd numbers from 1 to 1000
for candidate in range(1,1001,2):
	prime = 0
	# take the odd number and try to divide it by each number up to half of the canditate
	# print 'odd / 2: ', candidate / 2
	for denominator in range(2, candidate / 2):
		if candidate % denominator != 0:
			prime = 1
		else:
			prime = 0
			break		
	if prime == 1:
		print 'prime: ', candidate

