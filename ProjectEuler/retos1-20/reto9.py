"""
A Pythagorean triplet is a set of three natural numbers, 
a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
if __name__ == "__main__":
	for i in range(1000):
		for j in range(1000):
			if ((i+1)+(j+1)) == (1000 - math.sqrt((i+1)**2+(j+1)**2)):
				print (i+1)*(j+1)*(math.sqrt((i+1)**2+(j+1)**2))
				break
