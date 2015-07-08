# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def Fib(i, precachedList):
    if len(precachedList) > i:
        return precachedList[i]

    if i == 0 or i == 1:
        return 1
    else:
        value = precachedList[i - 1] + precachedList[i - 2]
        precachedList.append(value)


def GetFibonachAbowLimit(limit, precachedList):
    i = 0
    while True:
        i = i + 1
        Fib(i, precachedList)
        if precachedList[i] > limit:
            precachedList.remove(precachedList[i])
            break


def main():
    limit = 4000000
    fib = [0, 1, 1, 2, 3, 5, 8]
    GetFibonachAbowLimit(limit, fib)
    allEvenValuedNum = sum([fib[i] for i in xrange(0, len(fib)) if (i % 3 == 0)])

    print allEvenValuedNum


if __name__ == '__main__':
    main()
