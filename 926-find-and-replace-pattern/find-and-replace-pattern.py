class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            p_to_w = {}
            w_to_p = {}

            for p, w in zip(pattern, word):
                if p in p_to_w:
                    if p_to_w[p] != w:
                        return False
                else:
                    p_to_w[p] = w

                if w in w_to_p:
                    if w_to_p[w] != p:
                        return False
                else:
                    w_to_p[w] = p

            return True

        return [word for word in words if match(word)]