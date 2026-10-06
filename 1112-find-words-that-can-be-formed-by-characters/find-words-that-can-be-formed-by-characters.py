class Solution(object):
    def countCharacters(self, words, chars):
        char_count = [0] * 26

        for ch in chars:
            char_count[ord(ch) - ord('a')] += 1

        answer = 0

        for word in words:
            word_count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                word_count[index] += 1

            good = True

            for i in range(26):
                if word_count[i] > char_count[i]:
                    good = False
                    break

            if good:
                answer += len(word)

        return answer