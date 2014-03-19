def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA

	if n == 2:
		return listB
	
	listC = listA + listB

	return nth_fib_lists(listB, listC, n-1)


