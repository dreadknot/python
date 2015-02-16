# go through 1 to 100
for i in range(1, 101):
	s = str(i)
	# check if i is divisible by 3 or 5
	if i % 3 == 0 or i % 5 == 0:
		s = ''
		# if it's divisible by 3 add Fizz to string
		if i % 3 == 0:
			s = s + 'Fizz'
		# if it's divisible by 5 add Buzz to string
		if i % 5 == 0:
			s = s + 'Buzz'
	# print the sring, always with number, with Fizz, Buzz, or both.
	print s

