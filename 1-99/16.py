# /usr/bin python

from math import pow

def power_digit_sum(b, p):
    print [x for x in str(int(pow(2, p)))]
    return sum([int(x) for x in str(int(pow(2, p)))])

def main():
    print power_digit_sum(2, 1000)


main()