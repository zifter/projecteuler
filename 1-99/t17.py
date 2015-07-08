# /usr/bin python


mapped_number = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def lexical_cast(n):
    if n < 21:
        return mapped_number[n]
    elif n < 100:
        d = int(n/10)*10
        t = int(n %10)
        if t == 0:
            return mapped_number[d]
        else:
            return '%s %s' % (mapped_number[d], mapped_number[t])
    elif n == 100 or n == 1000:
        return '%s %s' %  (mapped_number[1], mapped_number[n])
    elif n < 1000:
        d = int(n/100)
        t = int(n%100)
        if t == 0:
            return '%s %s' % (mapped_number[d], mapped_number[100])
        else:
            return '%s %s and %s' % (mapped_number[d], mapped_number[100], lexical_cast(t))

def length_of_lexical_numbers(t, b):
    view = ''
    for i in range(t, b+1):
        view += lexical_cast(i)

    view = view.replace(' ', '')
    return len(view)


def main():
    print length_of_lexical_numbers(1, 1000)

if __name__ == '__main__':
    main()
