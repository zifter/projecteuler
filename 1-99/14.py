# /usr/bin python

g_sequence = {1: 1}


def get_sequence_length(n):
    global g_sequence

    if n in g_sequence:
        return g_sequence[n]

    l = get_sequence_length(n / 2 if n % 2 == 0 else 3 * n + 1) + 1
    g_sequence[n] = l
    return l


def process(limit):
    for i in xrange(1, limit + 1):
        get_sequence_length(i)

    max_v = 0
    max_k = 0
    for k, v in g_sequence.iteritems():
        if k <= limit and max_v < v:
            max_v = v
            max_k = k

    return max_v, max_k


def main():
    print process(1000000)[1]


main()
