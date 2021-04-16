from sys import stdin


class Matrix:
    def __init__(self, spis_i=[[]]):
        self.i = [i[:] for i in spis_i]

    def __str__(self):
        prius = ''
        for el in self.i:
            prius += '\t'.join(map(str, el)) + '\n'
        return prius.rstrip()

    def size(self):
        return (len(self.i), len(self.i[0]))

    def __add__(self, other):
        return



exec(stdin.read())
