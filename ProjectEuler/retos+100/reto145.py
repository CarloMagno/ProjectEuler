"""
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call 
such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?
"""
def reverse(num):
	res = 0
	while num>10:
		res = res*10 + num%10
		num = num/10
	res = res*10 + num
	return res

def oddAll(num):
	while(num!=0):
		if (num%10)%2==0:
			return False
		num = num/10
	return True

def reversible(n):
	if oddAll(reverse(n)+n):
		return True
	else:
		return False

if __name__ == "__main__":
	#MEMORYERROR
#	print len([i for i in range(1,10**9) if reversible(i)])
	num = 0
	for j in range(1,10**5):
		for i in range(1,10**4):
			if reversible(i*j):
				num+=1
	print num

#	print oddAll(1213)
#	print oddAll(1313)
#	print reversible(36)
#	print reverse(12345)
