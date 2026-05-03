class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        timer = 0
        cooldown = deque()
        heap = []

        # create max heap
        for value in freq.values():
            # why only the frequency and not the task? because we're only trying to find the least amount of time, not the order
            heapq.heappush(heap, -value)

        while heap or cooldown:
            if heap:
                # get the most frequently occuring value
                task = - heapq.heappop(heap)
                if task > 1:
                    # reduce the frequency and append to cooldown
                    # we're acknowledging this task
                    cooldown.append((task-1, timer+n+1))
            timer += 1

            # get items in cooldown that match the current time
            while cooldown and cooldown[0][1] == timer:
                task_count, next_iteration = cooldown.popleft()
                heapq.heappush(heap, -task_count)

        return timer