class Solution(object):
    def numSplits(self, s):
        n = len(s)

        # Frequency of characters in the right part
        right = [0] * 26

        for ch in s:
            right[ord(ch) - ord('a')] += 1

        left = [0] * 26

        left_distinct = 0
        right_distinct = sum(1 for x in right if x > 0)

        answer = 0

        # Split after every character except the last one
        for i in range(n - 1):
            index = ord(s[i]) - ord('a')

            # Move character from right to left
            if left[index] == 0:
                left_distinct += 1

            left[index] += 1

            right[index] -= 1

            if right[index] == 0:
                right_distinct -= 1

            # Check whether both parts have the same
            # number of distinct characters
            if left_distinct == right_distinct:
                answer += 1

        return answer
