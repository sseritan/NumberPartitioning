#/usr/bin/env python

import sys

def generate_set(N, K):
	""" Generate sets of numbers for number partitioning problem

	Args:
		N (int): Number of integers in both sets
		K (int): Total sum
	"""



if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: ./{} <number of integers> <subset sum>'.format(sys.argv[0]))

	generate_set(sys.argv[1])