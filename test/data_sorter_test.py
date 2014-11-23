#!/usr/bin/python

from java_interface import *

from random import randrange
from unittest import TestCase, skip
import unittest
from os import path


class DataSorterTest(TestCase):
	@skip("Too time consuming")
	def test_functionality(self):
		for _ in range(100):
			size = randrange(10000)
			values = generate_data(size)
			sorted_values = sort_data(values).values
			self.assertEquals(size, len(sorted_values))

			values.sort()
			self.assertEqual(values, sorted_values)

	@skip("fails")
	def test_remove_file_on_failure(self):
		open("output.txt").close()
		invoke_data_generator("input.txt", 5)
		invoke_data_sorter("input.txt", "output.txt", 1, 1, 10000)
		self.assertFalse(path.exists("output.txt"))

	@skip("fails")
	def test_primary_failure(self):
		for _ in range(100):
			result = generate_and_sort_data(
				randrange(10000),
				primary_failure_rate=1
			)
			self.assertFalse(result.primary_succeeded)
			self.assertTrue(result.secondary_succeeded)

	@skip("fails")
	def test_secondary_failure(self):
		for _ in range(100):
			while True:
				result = generate_and_sort_data(
					randrange(10000),
					primary_failure_rate=1,
					secondary_failure_rate=1,
				)
				# Avoid primary successes interfering with result
				if not result.primary_succeeded:
					break
			self.assertFalse(result.secondary_succeeded)

	@skip("passes")
	def test_primary_timeout(self):
		for _ in range(10):
			result = generate_and_sort_data(
				randrange(50000, 100000),
				primary_failure_rate=0,
				secondary_failure_rate=0,
				timeout=1
			)
			self.assertFalse(result.primary_succeeded)

	@skip("fails")
	def test_secondary_timeout(self):
		for _ in range(10):
			while True:
				result = generate_and_sort_data(
					randrange(50000, 100000),
					primary_failure_rate=1,
					secondary_failure_rate=0,
					timeout=1
				)
				if not result.primary_succeeded:
					break
			self.assertFalse(result.secondary_succeeded)
				

if __name__ == "__main__":
	unittest.main()

