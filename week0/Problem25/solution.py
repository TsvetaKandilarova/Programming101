def groupby(func, seq):
	dict_ = {}
	for item in seq:
		if not func(item) in dict_:
			dict_[func(item)] = [item]
		else:
			dict_[func(item)].append(item)
	return dict_
	list_ = [] + 'spam' * n
