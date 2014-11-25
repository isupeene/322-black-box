#!/usr/bin/python

from java_interface import *
from random import randrange
from time import time

def run():
	for _ in range(1000):
		num = randrange(10000000)
		before = time()
		invoke_data_generator(DATA_GENERATOR_OUTPUT, num)
		after = time()
		print("{}, {}".format(num, after - before))

if __name__ == "__main__":
	run()

