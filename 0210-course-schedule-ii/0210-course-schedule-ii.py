class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map of prereqs for each course
        graph = defaultdict(list)
        # num prereqs for each course
        indegree = [0]*numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # only queue courses with no prereqs
        queue = deque([i for i in range(numCourses) if indegree[i]==0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:    # check if all prereqs for the course are met
                    queue.append(child)
        
        return order if len(order) == numCourses else []

