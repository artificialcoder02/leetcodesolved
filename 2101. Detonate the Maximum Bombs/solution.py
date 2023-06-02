class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node: int, visited: set = None) -> set:
            if visited is None:
                visited = {node}

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

            return visited

        graph = defaultdict(set)

        for i, (x1, y1, rad) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= rad ** 2:
                    graph[i].add(j)

        return max(len(dfs(i)) for i in range(len(bombs)))
