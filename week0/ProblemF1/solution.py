import sys

def cat (file_name):
	file = open(file_name, "r")
	contents = file.read()

	file.close()

	return contents


