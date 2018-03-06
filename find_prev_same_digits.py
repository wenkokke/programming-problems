# Given a number n, find the largest number just smaller than n that can be
# formed using the same digits as n.

# So to solve this problem we want to find the first place in the number
# where one digit is smaller than the one, so that we can swap them, e.g.
#
#    208374928303 --> 208374928033
#
# So walking over the digits, left to right, find the first situation where
# the right digit is smaller than the left digit, and swap them.

# O(|n|)
def find_prev_same_digits(n):
    changed = False
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1, 1, -1):
        if digits[i] < digits[i - 1]:
            temp = digits[i]
            digits[i] = digits[i - 1]
            digits[i - 1] = temp
            changed = True
            break
    if not changed:
        raise ValueError(
            "%d is the smallest number with these digits" % (n,))
    return int(''.join(str(d) for d in digits))

if __name__ == "__main__":
    print find_prev_same_digits(208374928303)
