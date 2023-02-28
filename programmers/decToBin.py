def decToBin(src: int):
    dest = ''

    while src > 0:
        dest = str(src % 2) + dest
        src //= 2

    return dest