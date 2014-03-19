def number_to_list(n):
	list_ = []
	while n > 0:
		list_.append(n % 10)
		n //= 10
	return list_[::-1]

