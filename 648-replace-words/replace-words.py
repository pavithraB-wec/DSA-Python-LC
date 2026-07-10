class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        roots = set(dictionary)
        result = []

        for word in sentence.split():
            replacement = word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    replacement = prefix
                    break
            result.append(replacement)

        return " ".join(result)