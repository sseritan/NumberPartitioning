#!/usr/bin/env python

from collections_extended import bag
import random
import sys

def generate_set(N, K):
	""" Generate sets of numbers for number partitioning problem

	Args:
		N (int): Total number of integers
		K (int): Total sum
	"""
	if N < 2:
		raise RuntimeError('Should be more than 2 numbers')

	# Initialize sets with subset totals
	setA = bag([K // 2])
	setB = bag([K // 2 + K%2])


	# Go through and subdivide one set
	while len(setA) + len(setB) != N:
		# Randomly pick a number in a set
		target_set = random.choice([setA, setB])
		target_number = random.choice(list(target_set))

		try:
			new_el = random.randint(1, target_number-1)
			remainder = target_number - new_el

			# Subset sum logic
			print('Sets before change: {} {}'.format(setA, setB))
			target_set.remove(target_number)
			target_set.add(new_el)
			target_set.add(remainder)
			print('Sets after change: {} {}'.format(setA, setB))
		except:
			continue

	return setA, setB

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: ./{} <number of integers> <total sum>'.format(sys.argv[0]))

	N = int(sys.argv[1])
	K = int(sys.argv[2])

	A, B = generate_set(N, K)
	print('Set A: {} (total: {})'.format(A, sum(A)))
	print('Set B: {} (total: {})'.format(B, sum(B)))