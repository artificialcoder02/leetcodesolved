class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #start at city 0
        #recursively reach the neighbours
        #check outgoing edges

        edges = {(a,b) for a,b in connections}
        neighbours = {city:[] for city in range(n)}
        #we want to reach each node once
        visit=set()
        #count the number of edges to change
        changes=0

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        #traverse the graph recursively
        def dfs(city):
            #use nonlocal variable call so that we dont need to pass args to function call
            nonlocal edges , neighbours,visit, changes

            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                #check if this neighbour can reach city 0
                if(neighbour,city) not in edges:
                    changes+=1
                visit.add(neighbour)
                dfs(neighbour)
        visit.add(0)
        dfs(0)
        return changes

