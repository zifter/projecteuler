# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math


def prime_at(index):
    multiples = []
    primes = [1]

    low = 2
    up = index * 11

    for i in xrange(low, up):
        if i not in multiples:
            multiples.extend(xrange(i, up, i))
            primes.append(i)

    return primes[index]


def main():
    print prime_at(10001)


main()
