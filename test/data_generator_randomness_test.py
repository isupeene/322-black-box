#!/usr/bin/python

from __future__ import division
from java_interface import *
from scipy import stats


failures = 0
for _ in range(100):
	buckets = [0]*2**12
	for value in generate_data(2**16):
		buckets[value//2**20 + 2**11] += 1

	# Compute the chi-squared statistic as the sum of the squared
	# errors over the expected value.
	expected = 16
	chi2 = sum([
		(observation - expected)**2 / expected
		for observation in buckets
	])

	# Compute p-value given the chi-squared statistic.
	# The number of degrees of freedom is the number of
	# buckets minus 1.
	# Multiply by 2, as this is a 2-tailed test.
	p = (1 - stats.chi2.cdf(chi2, 2**12 - 1)) * 2

	if p < 0.1:
		failures += 1
print(failures)

