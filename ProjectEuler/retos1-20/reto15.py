#!usr/bin/env python
"""
Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.-

How many routes are there through a 20x20 grid?
"""
def factorial(n):
	res = 1
	for i in range(1,n+1):
		res *= i
	return res
	
def combinatorio(n,m):
	res = factorial(n)/(factorial(m)*factorial(n-m))
	return res

if __name__ == "__main__":
	print combinatorio(40,20)
