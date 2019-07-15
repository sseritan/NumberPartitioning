#!/usr/bin/env python

from collections_extended import bag # multiset implementation
import random
import sys

from IntegerPartitions import partitions


def generate_set(N, K):
	""" Generate sets of numbers for number partitioning problem

	Args:
		N (int): Total number of integers
		K (int): Total sum
	"""
	if N < 2:
		raise RuntimeError('Should be more than 2 numbers for set split')

	for p in partitions(K):
		for q in partitions(K):
			if len(p) + len(q) == K:
				print("Allowed partition: {} {}".format(p, q))

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: ./{} <number of integers> <total sum>'.format(sys.argv[0]))

	N = int(sys.argv[1])
	K = int(sys.argv[2])

	generate_set(N, K)