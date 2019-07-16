#!/usr/bin/env python

from collections import Counter
import random
import sys

from IntegerPartitions import partitions


# use a binary number (represented as string) as a mask
def mask(lst, m):
    # pad number to create a valid selection mask 
    # according to definition in the solution laid out 
    m = m.zfill(len(lst))
    return [el for el, flag in zip(lst, m) if flag != '0']
    #return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

def get_subset_sums(lst):
    subsums = {}
    # there are 2^n-1 binary numbers with length of the original list
    for i in range(1, 2**len(lst)):
        # create the pick corresponsing to current number
        mask_str = bin(i)[2:]
        pick = mask(lst, mask_str)
        subsums[mask_str] = sum(pick)
    return subsums

def generate_set(num_ints, total_sum):
    """ Generate sets of numbers for number partitioning problem

    Args:
        num_ints (int): Total number of integers
        total_sum (int): Total sum
    """
    if num_ints < 2:
        raise RuntimeError('Should be more than 2 numbers for set split')

    sets1 = []
    sets2 = []
    for p in partitions(total_sum // 2):
        # Skip if any repeats
        if any([v != 1 for v in Counter(p).values()]):
            #print('Skipped {} due to repeats'.format(p))
            continue

        for q in partitions(total_sum // 2 + total_sum%2):
            # Skip if any repeats
            if any([v != 1 for v in Counter(q).values()]):
                #print('Skipped {} due to repeats'.format(q))
                continue

            # Check for subset sums matching across partitions (i.e. degeneracy)
            subsum1 = get_subset_sums(p)
            subsum2 = get_subset_sums(q)
            matching_subsums = [ss for ss in subsum1.values() if ss in subsum2.values() and ss != total_sum // 2]
            if len(matching_subsums):
                #print('Skipped {} and {} due to matching subset sum of {}'.format(p, q, matching_subsums[0]))
                continue

            # Match number of integers asked for
            if len(p) + len(q) == num_ints:
                #print("!!! Allowed partition: {} {}".format(p, q))
                sets1.append(list(p))
                sets2.append(list(q))
            #else:
            #    print('Skipped {} and {} due to wrong number of integers ({} instead of {})'.format(p, q, len(p)+len(q), num_ints))

    print('\nAllowed partitions that total sum to {} with {} integers:'.format(total_sum, num_ints))
    for p, q in zip(sets1, sets2):
        print('{} {}'.format(p, q))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./{} <number of integers> <total sum>'.format(sys.argv[0]))

    num_ints = int(sys.argv[1])
    total_sum = int(sys.argv[2])

    generate_set(num_ints, total_sum)