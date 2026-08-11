class Solution(object):
    def minAddToMakeValid(self, s):
        open_count = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    # Need to insert '('
                    ans += 1

        # Remaining '(' need ')'
        ans += open_count

        return ans