class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}
        seen = set()

        for course, preq in prerequisites:
            graph[course].append(preq)

        def dfs(course):
            if course in seen:
                return False
            if  graph[course] == []:
                return True
            seen.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False

            seen.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    


