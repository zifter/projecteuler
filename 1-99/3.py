# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math


def eratosthenes(limit):
    limitSQRT = int(math.sqrt(limit)) + 1
    multiples = [1]
    primeFactors = []
    redLimit = limit

    for i in xrange(2, limitSQRT):
        if i not in multiples:
            multiples.extend(xrange(i * i, limitSQRT, i))
            # prime number
            if redLimit % i == 0:
                primeFactors.append(i)
                redLimit = redLimit / i
                if redLimit in multiples:
                    break

    return primeFactors


def main():
    primeFactors = eratosthenes(int(600851475143))
    print primeFactors[-1]


if __name__ == '__main__':
    main()
