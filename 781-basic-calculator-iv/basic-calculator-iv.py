from collections import Counter

class Poly(Counter):
    def __add__(self, other):
        res = Poly(self)
        for k, v in other.items():
            res[k] += v
            if res[k] == 0:
                del res[k]
        return res

    def __sub__(self, other):
        res = Poly(self)
        for k, v in other.items():
            res[k] -= v
            if res[k] == 0:
                del res[k]
        return res

    def __mul__(self, other):
        res = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                key = tuple(sorted(k1 + k2))
                res[key] += v1 * v2
                if res[key] == 0:
                    del res[key]
        return res

class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        values = dict(zip(evalvars, evalints))

        def make(token):
            poly = Poly()
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                poly[()] = int(token)
            elif token in values:
                poly[()] = values[token]
            else:
                poly[(token,)] = 1
            return poly

        def parse(tokens):
            def factor():
                if tokens[0] == '(':
                    tokens.pop(0)
                    node = expr()
                    tokens.pop(0)
                    return node
                return make(tokens.pop(0))

            def term():
                node = factor()
                while tokens and tokens[0] == '*':
                    tokens.pop(0)
                    node = node * factor()
                return node

            def expr():
                node = term()
                while tokens and tokens[0] in ('+', '-'):
                    op = tokens.pop(0)
                    if op == '+':
                        node = node + term()
                    else:
                        node = node - term()
                return node

            return expr()

        # Tokenize
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif expression[i] in '()+-*':
                tokens.append(expression[i])
                i += 1
            else:
                j = i
                while j < len(expression) and expression[j].isalnum():
                    j += 1
                tokens.append(expression[i:j])
                i = j

        poly = parse(tokens)

        result = []

        for vars_, coef in sorted(poly.items(),
                                  key=lambda x: (-len(x[0]), x[0])):
            if coef == 0:
                continue
            if vars_:
                result.append(str(coef) + "*" + "*".join(vars_))
            else:
                result.append(str(coef))

        return result