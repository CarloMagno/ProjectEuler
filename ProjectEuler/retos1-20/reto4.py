"""
A palindromic number reads the same both ways. The largest palindrome
 made from the product of two 2-digit numbers is 9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def capicuo(n):
	numero = str(n)
	if numero == numero[::-1]:
		return True
	else:
		return False

if __name__ == "__main__":
	print max([i*j for i in reversed(range(100,1000)) for j in reversed(range(100,1000)) if capicuo(i*j)])
