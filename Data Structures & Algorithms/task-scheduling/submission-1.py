import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        # (remaining_count, ready_time)
        q = deque()

        time = 0

        while heap or q:
            time += 1

            # FIRST: release task whose cooldown is over
            if q and q[0][1] == time:
                cnt, ready_time = q.popleft()
                heapq.heappush(heap, cnt)

            # THEN: execute a task
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1

                if cnt < 0:
                    q.append((cnt, time + n + 1))

        return time