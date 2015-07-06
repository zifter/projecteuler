# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def eratosthenes(limit):
    prime = [True] * limit
    prime[0] = False  # 0 is not a prime
    prime[1] = False  # 1 is not a prime

    for i in xrange(2, limit):
        if prime[i]:
            notPrime = xrange(i, limit, i)
            for x in notPrime:
                prime[x] = False

            prime[i] = True  # hack

    primesFactors = []
    for i in xrange(0, limit):
        if prime[i]:
            primesFactors.append(i)
    return primesFactors


def main():
    print sum(eratosthenes(int(2000000)))


main()
