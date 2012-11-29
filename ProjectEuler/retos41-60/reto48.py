#!/usr/bin/env/ python
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
import sys

if __name__ == "__main__":
	sum = 0
	num = 1000
	for i in range (num):
		if i!=0:
			sum += i**i

	print sum%(10**10)
