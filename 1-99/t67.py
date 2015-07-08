# /usr/bin python

from t18 import *

def main():
    finder = MaxRouteFinder(load_triagle('67.txt'))
    print finder.get_answer()


if __name__ == '__main__':
    main()
