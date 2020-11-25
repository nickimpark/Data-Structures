import numpy as np
pi = 3.1415

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __eq__(self, other):
        return (self.re == other.re) and (self.im == other.im)
    
    def __str__(self):
        return str(self.re) + (' + ' + str(self.im) + 'i') * bool(self.im)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
            return Complex(re, im)
        elif isinstance(other, int) or isinstance(other, float):
            re = self.re * other
            im = self.im * other
            return Complex(re, im)
    
    __rmul__ = __mul__

    def __abs__(self):
        return np.sqrt(self.re ** 2 + self.im ** 2)
    
    def arg(self):
        if self.re > 0:
            return np.arctan(self.im / self.re)
        elif self.re == 0:
            if self.im > 0:
                return pi/2
            elif self.im < 0:
                return -pi/2
            else:
                return 0
        elif self.im >= 0:
            return np.arctan(self.im / self.re) + pi
        elif self.im < 0:
            return np.arctan(self.im / self.re) - pi
    
    def arg_deg(self):
        return self.arg()*(180/pi)
