class Solution:
    def distanceLimitedPathsExist(self, length: int, adjList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(length)]
        rank = [0 for i in range(length)]
        weight = [0 for i in range(length)]

        adjList.sort(key=lambda x: x[2])
        for edge in adjList:
            self.unionByRank(edge[0], edge[1], edge[2], parent, rank, weight)

        answer = []
        for query in queries:
            answer.append(self.isConnectedAndWithinLimit(query[0], query[1], query[2], parent, weight))

        return answer

    def isConnectedAndWithinLimit(self, p: int, q: int, limit: int, parent: List[int], weight: List[int]) -> bool:
        return self.find(p, limit, parent, weight) == self.find(q, limit, parent, weight)

    def find(self, x: int, limit: int, parent: List[int], weight: List[int]) -> int:
        while x != parent[x]:
            if weight[x] >= limit:
                break
            x = parent[x]
        return x

    def unionByRank(self, x: int, y: int, limit: int, parent: List[int], rank: List[int], weight: List[int]) -> None:
        x_ref = self.find(x, float('inf'), parent, weight)
        y_ref = self.find(y, float('inf'), parent, weight)
        if x_ref != y_ref:
            if rank[x_ref] < rank[y_ref]:
                parent[x_ref] = y_ref
                weight[x_ref] = limit
            else:
                parent[y_ref] = x_ref
                weight[y_ref] = limit
                if rank[x_ref] == rank[y_ref]:
                    rank[x_ref] += 1
