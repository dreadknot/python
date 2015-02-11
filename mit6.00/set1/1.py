
# add the only even prime 2 to the list of primes
primes = [2]
# go through all the odd numbers from 1 to 1000
for candidate in range(1,1001,2):
	# assume each candidate is prime
	prime = 1
	# take the odd number and try to divide it by each number up to half of the canditate
	# print 'odd / 2: ', candidate / 2
	for denominator in range(2, candidate / 2):
		# if remainder is 0 candidate is not prime and can stop checking
		if candidate % denominator == 0:
			prime = 0
			break
		# else it's still prime
		else:
			prime = 1	
	# if prime has remaind true, this canditate is prime append to the list of primes
	if prime == 1:
		primes.append(candidate)

# print a sorted list of the primes
print sorted(primes)

