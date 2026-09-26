import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, index, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next