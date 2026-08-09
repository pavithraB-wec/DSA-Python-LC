class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        
        # Step 2: get max subsequence of length k
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k
            
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            
            return stack[:k]

        # Step 3: merge two sequences
        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        m, n = len(nums1), len(nums2)
        best = []

        # Step 1: try all splits
        for i in range(max(0, k - n), min(k, m) + 1):
            seq1 = maxSubsequence(nums1, i)
            seq2 = maxSubsequence(nums2, k - i)

            candidate = merge(seq1[:], seq2[:])
            best = max(best, candidate)

        return best