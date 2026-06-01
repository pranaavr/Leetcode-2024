class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre = defaultdict(list) # track what courses the key is a prereq for
        indegrees = [0]*numCourses
        for u, v in prerequisites:
            pre[v].append(u)
            indegrees[u] += 1   # how many prereqs the coursse has
        
        q = deque() # tracking for course with all prereqs met

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for course in pre[cur]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)
        
        return res if sum(indegrees) == 0 else []