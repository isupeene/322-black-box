#!/usr/bin/python

from java_interface import *

from random import randrange
from unittest import TestCase, skip
import unittest

class DataGeneratorTest(TestCase):
	@skip("Too time consuming.")
	def test_functionality(self):
		for _ in range(100):
			size = randrange(10000)
			self.assertEqual(size, len(generate_data(size)))

	@skip("Fails")
	def test_negative_size(self):
		self.assertIn(
			"Error",
			invoke_data_generator(DATA_GENERATOR_OUTPUT, -1)[0]
		)

	#@skip("Passes")
	def test_no_access(self):
		self.assertIn(
			"Error",
			invoke_data_generator("restricted.txt", 5)[0]
		)
		self.assertIn(
			"Error",
			invoke_data_generator("restricted/output.txt", 5)[0]
		)

if __name__ == '__main__':
	unittest.main()

