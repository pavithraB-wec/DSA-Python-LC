class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                # Move slow one step
                nxt = next_index(slow)
                if nums[nxt] == 0 or (nums[nxt] > 0) != direction:
                    break
                slow = nxt

                # Move fast first step
                nxt = next_index(fast)
                if nums[nxt] == 0 or (nums[nxt] > 0) != direction:
                    break
                fast = nxt

                # Move fast second step
                nxt = next_index(fast)
                if nums[nxt] == 0 or (nums[nxt] > 0) != direction:
                    break
                fast = nxt

                if slow == fast:
                    # Reject one-element loop
                    if slow == next_index(slow):
                        break
                    return True

            # Mark visited nodes as 0
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False