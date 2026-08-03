class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort by height descending, then k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        for person in people:
            queue.insert(person[1], person)

        return queue