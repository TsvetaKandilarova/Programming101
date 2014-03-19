import sys

def concat_files(filenames):
	MEGATRON = open("MEGATRON", "a")

	for filename in filenames:
		file_ = open(filename, "r")
		MEGATRON.write(file_.read())
		MEGATRON.write("\n\n")
		file_.close()

	MEGATRON.close()

if __name__ == '__main__':
	main()