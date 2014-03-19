def prime_factorization(n):
	numbers = []
	pows 	= []
	count 	= 0
	while n > 1:
		for i in range(2,n+1):
			if n % i == 0:
				numbers.append(i)
				count += 1
				n /= i
				while n % i == 0:
					count += 1
					n /= i
				pows.append(count)
			count = 0
		
	str = []
	for i in range(0,len(numbers)):
		str.append((numbers[i],pows[i]))
	return str

def main ():
	print (prime_factorization(10))
if __name__ == '__main__':
	main()	 	
