from collections import defaultdict

class Solution(object):

    def validArrangement(self, pairs):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            outdegree[start] += 1
            indegree[end] += 1

        start_node = pairs[0][0]

        for node in outdegree:
            if outdegree[node] - indegree[node] == 1:
                start_node = node
                break

        result = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)

            result.append(node)

        dfs(start_node)

        result.reverse()

        answer = []

        for i in range(len(result) - 1):
            answer.append([result[i], result[i + 1]])

        return answer