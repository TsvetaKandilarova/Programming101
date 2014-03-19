def prepare_meal(number):
	n = 0
	for i in range (1,number):
		if number % (3**i) == 0:
			n = i
	list_ = "spam " * n
	if number % 5 == 0:
		if not len(list_) == 0:
			list_ = list_ + "and eggs"
		else:
			list_ = "eggs"
	return list_

