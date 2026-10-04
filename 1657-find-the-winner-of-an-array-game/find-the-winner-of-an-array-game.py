class Solution(object):
    def getWinner(self, arr, k):
        winner = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]
                wins = 1

            if wins == k:
                return winner

        return winner