# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def process(limit):
    numberOf3 = (limit - 1) / 3
    numberOf5 = (limit - 1) / 5

    sumOfAll3 = sum([i * 3 for i in xrange(1, numberOf3 + 1)])
    sumOfAll5 = sum([i * 5 for i in xrange(1, numberOf5 + 1) if (i % 3 != 0)])

    return sumOfAll3 + sumOfAll5


def main():
    print process(1000)


main()
