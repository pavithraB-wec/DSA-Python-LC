class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            result = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                result.append(l + r)
                            elif ch == "-":
                                result.append(l - r)
                            else:
                                result.append(l * r)

            if not result:
                result.append(int(expr))

            memo[expr] = result
            return result

        return solve(expression)