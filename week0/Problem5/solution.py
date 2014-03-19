def count_divisors(n):
	count_ = 0
	for i in range(1,n + 1):
		if (n % i == 0):
			count_ += 1
	return count_

def sum_of_divisors(n):
	sum_ = 0
	for i in range(1,n + 1):
		if (n % i == 0):
			sum_ += i 
	return sum_

def is_prime(n):
	c = sum_of_divisors(n)
	if c == n + 1:
		return True
	return False

def prime_number_of_divisors(n):
	return is_prime(count_divisors(n))
