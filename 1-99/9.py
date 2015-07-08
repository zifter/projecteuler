# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math


def main():
    triplets = set()
    for i in xrange(1, 500):
        for j in xrange(1, i + 500):
            if i * i + j * j == (1000 - i - j) * (1000 - i - j):
                triplets.add(i * j * (1000 - i - j))

    print triplets


if __name__ == '__main__':
    main()
