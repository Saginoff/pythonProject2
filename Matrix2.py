from sys import stdin


class Matrix:
    def __init__(self, spis_i=[[]]):
        self.m = [i[:] for i in spis_i]

    def __str__(self):
        prius = ''
        for el in self.m:
            prius += '\t'.join(map(str, el)) + '\n'
        return prius.rstrip()

    def size(self):
        return (len(self.m), len(self.m[0]))

    def __add__(self, other):
        ri, rj = range(len(self.m)), range(len(self.m[0]))
        return Matrix([[self.m[i][j] + other.m[i][j] for j in rj] for i in ri])

    def __mul__(self, skalar):
        ri, rj = range(len(self.m)), range(len(self.m[0]))
        return Matrix([[self.m[i][j] * skalar for j in rj] for i in ri])

    __rmul__ = __mul__


exec(stdin.read())
