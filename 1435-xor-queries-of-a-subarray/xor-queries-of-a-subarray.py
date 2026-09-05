class Solution(object):
    def xorQueries(self, arr, queries):
        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] ^ num)

        answer = []

        for left, right in queries:
            answer.append(prefix[right + 1] ^ prefix[left])

        return answer