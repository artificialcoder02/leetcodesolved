class Solution:
    def detectCycle(self, v, src, rst, vis):
        vis[src] = 1
        rst[src] = 1
        for x in v[src]:
            if vis[x] == 0 and self.detectCycle(v, x, rst, vis):
                return True
            elif rst[x] == 1:
                return True
        rst[src] = 0
        return False

    def canFinish(self, numCourses, prerequisites):
        v = [[] for _ in range(numCourses)]
        vis = [0] * numCourses
        rst = [0] * numCourses
        for x in prerequisites:
            v[x[1]].append(x[0])
        for i in range(numCourses):
            if vis[i] == 0 and self.detectCycle(v, i, rst, vis):
                return False
        return True
