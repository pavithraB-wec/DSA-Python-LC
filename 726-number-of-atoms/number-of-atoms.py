from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if start < i else 1

                top = stack.pop()
                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mult

            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1

                stack[-1][atom] += count

        result = []
        for atom in sorted(stack[-1]):
            result.append(atom)
            if stack[-1][atom] > 1:
                result.append(str(stack[-1][atom]))

        return "".join(result)