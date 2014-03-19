def is_int_palindrome(n):
	temp = str(n)
	return temp == temp[::-1]

if __name__ == '__main__':
	main()
