from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)

        # Replace punctuation with spaces
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.lower().split()

        count = Counter()

        for word in words:
            if word not in banned:
                count[word] += 1

        return count.most_common(1)[0][0]