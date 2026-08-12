class Solution(object):
    def strWithout3a3b(self, a, b):
        result = []

        while a > 0 or b > 0:
            # Last two characters are "aa", so we must use b
            if len(result) >= 2 and result[-1] == 'a' and result[-2] == 'a':
                result.append('b')
                b -= 1

            # Last two characters are "bb", so we must use a
            elif len(result) >= 2 and result[-1] == 'b' and result[-2] == 'b':
                result.append('a')
                a -= 1

            # Otherwise, use the character with more remaining
            elif a >= b:
                result.append('a')
                a -= 1

            else:
                result.append('b')
                b -= 1

        return ''.join(result)