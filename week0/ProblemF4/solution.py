import sys

def sum_numbers(filename):
	file = open (filename, "r")
	contents = file.read().split(" ")

	file.close()

	sum = 0

	for i in range(0,len(contents)):
		sum += int(contents[i])

	return sum

def main():
	print (sum_numbers(sys.argv[1]))

if __name__ == '__main__':
	main()