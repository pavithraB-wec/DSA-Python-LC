class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        below20 = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            elif n < 1000:
                return below20[n // 100] + " Hundred " + helper(n % 100)
            elif n < 1000000:
                return helper(n // 1000) + "Thousand " + helper(n % 1000)
            elif n < 1000000000:
                return helper(n // 1000000) + "Million " + helper(n % 1000000)
            else:
                return helper(n // 1000000000) + "Billion " + helper(n % 1000000000)

        return helper(num).strip()