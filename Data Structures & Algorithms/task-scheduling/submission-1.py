from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        heap = []
        cooldown = deque()
        cycle = 0

        # Count frequency
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        # Max heap: (-frequency, task)
        for task, freq in count.items():
            heapq.heappush(heap, (-freq, task))

        while heap or cooldown:

            # Move tasks whose cooldown is finished back to heap
            while cooldown and cooldown[0][2] <= cycle:
                task, freq, available_time = cooldown.popleft()
                heapq.heappush(heap, (-freq, task))

            # Execute a task if available
            if heap:
                neg_freq, task = heapq.heappop(heap)

                freq = -neg_freq
                freq -= 1

                if freq > 0:
                    cooldown.append((task, freq, cycle + n + 1))

            # One unit of time passes
            cycle += 1

        return cycle