class Complex:
    def __init__(self, x=0, y=0):
        self.re = x
        self.im = y

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep
'''
    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)
'''

a = Complex(1, 2)
b = Complex(3, -4.5)
print(a)
print(b)
#print(a + b)