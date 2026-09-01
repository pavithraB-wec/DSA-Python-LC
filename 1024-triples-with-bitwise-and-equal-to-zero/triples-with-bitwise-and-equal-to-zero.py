class Solution(object):
    def countTriplets(self, nums):
        MAX = 1 << 16

        # Frequency of each number
        freq = [0] * MAX

        for x in nums:
            freq[x] += 1

        # Count pairs (i, j) by their AND result
        pair = [0] * MAX

        for a in range(MAX):
            if freq[a] == 0:
                continue

            for b in range(MAX):
                if freq[b] == 0:
                    continue

                value = a & b
                pair[value] += freq[a] * freq[b]

        # Add the third element
        answer = 0

        for value in range(MAX):
            if pair[value] == 0:
                continue

            for x in nums:
                if (value & x) == 0:
                    answer += pair[value]

        return answer
