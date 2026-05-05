class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        timer = 0
        freqs = Counter(tasks)
        heap = [] # should only hold available tasks
        cooldown = deque()

        for val in freqs.values():
            heapq.heappush(heap, -val)

        while heap or cooldown:
            timer += 1
            if heap:
                val = heapq.heappop(heap) + 1
                if val != 0:
                    cooldown.append((val, timer+n))

            if cooldown and cooldown[0][1] <= timer:
                heapq.heappush(heap, cooldown.popleft()[0])

        return timer

        