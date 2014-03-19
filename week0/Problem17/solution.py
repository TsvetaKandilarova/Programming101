def slope_style_score (scores):
	min = scores[0]
	max = scores[0]
	for item in scores:
		if (item < min):
			min = item
		if (item > max):
			max = item
	return (sum(scores) - (min + max)) / (len(scores)-2)

