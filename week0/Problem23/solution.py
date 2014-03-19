def count_words (arr):
	dict_ = {}
	for item in arr:
		if not item in dict_:
			dict_[item] = 1
		else:
			dict_[item] = dict_[item] + 1
	return dict_

			
