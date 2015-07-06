# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import itertools


def main():
    combs = list(itertools.combinations(xrange(1, 101), 2))

    print 2 * sum([p[0] * p[1] for p in combs])


main()
