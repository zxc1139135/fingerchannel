#coding=utf-8
"""
私钥共享算法程序
"""


from __future__ import division
from __future__ import print_function

import random
import functools

_PRIME = 2 ** 127 - 1


_RINT = functools.partial(random.SystemRandom().randint, 0)

"""
Evaluates polynomial (coefficient tuple) at x, used to generate a
shamir pool in make_random_shares below.
"""


def _eval_at(poly, x, prime):
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum


"""
Generates a random shamir pool, returns the secret and the share
points.
"""


def make_random_shares(minimum, shares, prime=_PRIME):
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [_RINT(prime) for i in range(minimum)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return poly[0], points


"""
Division in integers modulus p means finding the inverse of the
denominator modulo p and then multiplying the numerator by this
inverse (Note: inverse of A is B such that A*B % p == 1) this can
be computed via extended Euclidean algorithm
"""


def _extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y


"""
Compute num / den modulo prime p
To explain what this means, the return value will be such that
the following is true: den * _divmod(num, den, p) % p == num
"""


def _divmod(num, den, p):
    inv, _ = _extended_gcd(den, p)
    return num * inv


"""
Find the y-value for the given x, given n (x, y) points;
k points will define a polynomial of up to kth order.
"""


def _lagrange_interpolate(x, x_s, y_s, p):
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"

    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum

    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p


"""Recover the secret from share points (x, y points on the polynomial)"""


def recover_secret(shares, threshold, prime=_PRIME):
    if len(shares) < threshold:
        # raise ValueError("need at least threshold shares")
        # print("\nneed at least %d shares!" %threshold)
        return "need at least %d shares!" % threshold

    else:
        x_s, y_s = zip(*shares)
        return _lagrange_interpolate(0, x_s, y_s, prime)


"""Shamir Secret Sharing Scheme"""


def Shamir_Secret():
    print("\n----------------------------------------------------------------------")
    print("|       Shamir's Secret Sharing Scheme over Integer Arithmetic       |")
    print("----------------------------------------------------------------------")

    shares = int(input("Enter the number of Shares: "))
    threshold = int(input("Enter the threshold value: "))

    if (threshold > shares):
        print("Threshold value must be less or equal to shares value, please enter the correct threshold value")
        threshold = int(input("Enter the threshold value: "))

    secret, shares = make_random_shares(threshold, shares)

    print("\nSecret:                                                     ", secret)
    print("\nShares:")
    if shares:
        for share in shares:
            print('  ', share)

    print("\nSecret recovered from minimum subset of shares:             ",
          recover_secret(shares[:threshold], threshold))
    print("Secret recovered from a different minimum subset of shares: ",
          recover_secret(shares[(0 - threshold):], threshold))

    ns = int(input("Enter the number of shares to recover secret: "))
    print("Selected Shares:\n")
    for i in range(ns):
        print('  ', shares[i])
    print("\nSecret recovered from the given subset of shares:           ", recover_secret(shares[:ns], threshold))


if __name__ == '__main__':

    opt = "y";
    while opt == "y":
        Shamir_Secret()
        opt = input("Do you want to play more? (y/n): ")