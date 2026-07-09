class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        pos = {}

        for i, word in enumerate(list1):
            pos[word] = i

        ans = []
        best = float('inf')

        for j, word in enumerate(list2):
            if word in pos:
                s = pos[word] + j

                if s < best:
                    best = s
                    ans = [word]
                elif s == best:
                    ans.append(word)

        return ans