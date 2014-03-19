def count_vowels(str):
	count_ = 0
	vowels = ['a','e','o','u','i','y','A','E','O','U','I','Y']
	for i in range (0,len(str)):
		if str[i] in vowels:
			count_ += 1
	return count_
