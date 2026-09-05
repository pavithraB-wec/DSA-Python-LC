class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        freq = {}

        # Create frequency map of word masks
        for word in words:
            mask = 0

            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))

            # Count unique letters without bit_count()
            if bin(mask).count("1") <= 7:
                freq[mask] = freq.get(mask, 0) + 1

        answer = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))

            other = 0

            for ch in puzzle[1:]:
                other |= 1 << (ord(ch) - ord('a'))

            count = 0
            subset = other

            while True:
                mask = subset | first

                if mask in freq:
                    count += freq[mask]

                if subset == 0:
                    break

                subset = (subset - 1) & other

            answer.append(count)

        return answer