class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(expr):
            coef = 0
            const = 0
            i = 0
            sign = 1

            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j].isdigit():
                        j += 1

                    if j < len(expr) and expr[j] == 'x':
                        if i == j:
                            num = 1
                        else:
                            num = int(expr[i:j])
                        coef += sign * num
                        j += 1
                    else:
                        num = int(expr[i:j])
                        const += sign * num

                    i = j

            return coef, const

        left, right = equation.split('=')

        c1, n1 = parse(left)
        c2, n2 = parse(right)

        coef = c1 - c2
        const = n2 - n1

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"

        return "x=" + str(const // coef)