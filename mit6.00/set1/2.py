from math import * 

n = raw_input('Compute sum of log primes to: ')

# add the only even prime 2 to the list of primes
primes = [2]

# sum the log of primes
log_sum = 0
# go through all the odd numbers from 1 to 1000 with step 2
for candidate in range(1,int(n),2):
	# assume each candidate is prime
	prime = 1
	# take the odd number and try to divide it by each number up to half of the canditate
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
		log_sum = log_sum + log(candidate)
		primes.append(candidate)

# print a sorted list of the primes
print sorted(primes)

print 'sum log of primes: ', log_sum
print 'to n: ', n
print 'ratio: ', log_sum / int(n)