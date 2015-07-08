# /usr/bin python

from math import factorial

def factorial_digit_sum(n):
    return sum([int(x) for x in str(int(factorial(n)))])

def main():
    print factorial_digit_sum(100)


if __name__ == '__main__':
    main()