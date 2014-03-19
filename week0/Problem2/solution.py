def sum_of_min_and_max(arr):
	if len(arr) == 0:
		return 0
	else:
		min = arr[0]
		max = arr[0]
		for item in arr:
			if (item < min):
				min = item
			if (item > max):
				max = item
	return min + max
