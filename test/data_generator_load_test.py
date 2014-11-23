#!/usr/bin/python

from java_interface import *

if __name__ == "__main__":
	size = 1
	while True:
		print("Trying with {} values...".format(size))
		invoke_data_generator(DATA_GENERATOR_OUTPUT, size)
		print("Success!")
		size *= 2

