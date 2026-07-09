class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a, b = num1[:-1].split('+')
        c, d = num2[:-1].split('+')

        a, b = int(a), int(b)
        c, d = int(c), int(d)

        real = a * c - b * d
        imag = a * d + b * c

        return str(real) + "+" + str(imag) + "i"