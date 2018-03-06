# Given an integer array, output all pairs that sum up to a specific value k.

from __future__ import division

# O(|lst|)
def array_pair_sum(k, lst):

    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    retn = []
    # Assume: dict.items() returns the items sorted by key
    for i, total in count.items():
        if i > k // 2 + 1:
            break
        if k - i in count:
            for _ in range(0, max(total, count[k - i])):
                retn.append((i, k - i))

    return retn

if __name__ == "__main__":
    print array_pair_sum(9, [2, 3, 6, 4, 7, 2, 9])
