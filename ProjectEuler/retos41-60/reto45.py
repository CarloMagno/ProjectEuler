def triangle(n):
	return n*(n+1)/2

def pentagonal(n):
	return n*(3*n-1)/2
	
def hexagonal(n):
	return n*(2*n-1)

if __name__ == "__main__":
	Tset = set([triangle(i) for i in range(1,10**5)])
	Pset = set([pentagonal(i) for i in range(1,10**5)])
	Hset = set([hexagonal(i) for i in range(1,10**5)])
	
	Res = Tset.intersection(Pset)
	Res = Hset.intersection(Res)
	print Res
