class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        from collections import Counter

        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        old = self.nums2[index]

        self.freq[old] -= 1
        self.nums2[index] += val

        new = self.nums2[index]
        self.freq[new] += 1

    def count(self, tot):
        result = 0

        for num in self.nums1:
            complement = tot - num
            result += self.freq.get(complement, 0)

        return result