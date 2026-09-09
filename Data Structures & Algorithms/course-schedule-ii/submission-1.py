class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        order=[]

        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            indegree[course] += 1
            adj[prerequisite].append(course)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            node = q.popleft()
            order.append(node)
            count += 1

            for course in adj[node]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)
                

        
        return order if count == numCourses else []