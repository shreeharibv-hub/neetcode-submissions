class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses

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
            count += 1

            for course in adj[node]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)

        return count == numCourses