def is_increasing(arr):
	for i in range(0,len(arr)-1):
		if (arr[i] >= arr[i+1]):
			return False
	return True

