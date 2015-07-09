# /usr/bin python

import t10


class AmicableNumbersFinder():
    natural_number = []
    mapped_sum = dict()
    limit = 0
    def __init__(self, limit):
        self.natural_number = t10.eratosthenes(limit)
        self.limit = limit

    def get_sum(self):
        return sum(self.get_all_amicable_numbers())

    def get_all_amicable_numbers(self):
        answer = set()

        for i in xrange(1, self.limit+1):
            self.mapped_sum[i] = sum(self.get_devs(i))

        for k, v in self.mapped_sum.iteritems():
            if k!=v and v in self.mapped_sum and k == self.mapped_sum[v]:
                answer.add(k)

        print answer
        return answer

    def get_devs(self, n):
        halfNumber = n / 2

        primes = []

        i = 1
        while i <= halfNumber:
            if n % i == 0:
                primes.append(i)

                if n == 1:
                    break
            i = i + 1

        return primes


def main():
    finder = AmicableNumbersFinder(10000)
    print finder.get_sum()


if __name__ == '__main__':
    main()