# /usr/bin python

def load_triagle(path):
    t = []
    with open(path) as f:
        ls = f.readlines()
        for l in ls:
            t.append([int(x) for x in l.split()])
        return t

class MaxRouteFinder():
    def __init__(self, triangle):
        self.tr = triangle
        self.cache = {}

    def get_answer(self):
        return self.__find((0,0))

    def __find(self, pos):
        if pos in self.cache:
            return self.cache[pos]

        if pos[0] >= len(self.tr):
            return 0
        elif pos[0] >= len(self.tr[pos[0]]):
            return 0
        else:
            l = self.__find((pos[0]+1, pos[1]))
            r = self.__find((pos[0]+1, pos[1]+1))
            answer = max(l, r)+self.tr[pos[0]][ pos[1]]

        self.cache[pos] = answer
        return answer

def main():
    finder = MaxRouteFinder(load_triagle('18.txt'))
    print finder.get_answer()


main()
