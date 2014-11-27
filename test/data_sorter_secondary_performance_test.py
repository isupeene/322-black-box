#!/usr/bin/python

from java_interface import *
from random import randrange
from time import time

def run():
	for _ in range(1000):
		size = randrange(1000000)
		data = generate_data(size)
		while True:
			before = time()
			result = sort_data(data, primary_failure_rate=1)
			after = time()

			if result.secondary_succeeded:
				break

		print("{}, {}".format(size, after - before))

if __name__ == "__main__":
	run()
