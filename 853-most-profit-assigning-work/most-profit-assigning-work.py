class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        ans = 0
        best = 0
        i = 0

        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            ans += best

        return ans