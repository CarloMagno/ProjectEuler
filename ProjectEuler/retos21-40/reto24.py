from itertools import permutations

if __name__ == "__main__":
	permutaciones = list(permutations(range(10)))
	print permutaciones[(10**6)-1]
