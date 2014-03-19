def nth_fibonacci(n):
	a = 1
	b = 1
	k = 2
	while n > k:
		k += 1
		c = a
		a = b
		b = b + c
	return b
