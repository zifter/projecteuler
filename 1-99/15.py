# /usr/bin python

g_cache = {(1, 1): 2}


def get_pahtes_amount(squad):
    if squad in g_cache:
        return g_cache[squad]

    if squad[0] == 0 or squad[1] == 0:
        answer = 1
    else:
        answer = get_pahtes_amount((squad[0], squad[1]-1)) + get_pahtes_amount((squad[0]-1, squad[1]))

    g_cache[squad] = answer
    return answer


def main():
    print get_pahtes_amount((20, 20))


main()
