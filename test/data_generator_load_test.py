#!/usr/bin/python

from java_interface import *

if __name__ == "__main__":
	size = 1
	while True:
		print("Trying with {} values...".format(size))
		out, err = invoke_data_generator(DATA_GENERATOR_OUTPUT, size)
		if not err:
			print("Success!")
		else:
			print(err)
			break
		size *= 2

