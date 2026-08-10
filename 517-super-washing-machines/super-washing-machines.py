class Solution(object):
    def findMinMoves(self, machines):
        n = len(machines)
        total = sum(machines)
        
        if total % n != 0:
            return -1
        
        avg = total // n
        max_moves = 0
        flow = 0
        
        for m in machines:
            diff = m - avg
            flow += diff
            
            max_moves = max(max_moves, abs(flow), diff)
        
        return max_moves