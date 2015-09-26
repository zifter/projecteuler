# /usr/bin python

import t10




def main():
    with open('22.txt', 'r') as stream:
        data = stream.read()
        names = [x.replace('"', '') for x in data.split(',')]
    names.sort()

    answer = 0
    i = 0
    while i < len(names):
        s = sum([ord(ch) - ord('A') + 1 for ch in names[i]])
        answer += s *(i+1)
        i += 1

    print answer


if __name__ == '__main__':
    main()