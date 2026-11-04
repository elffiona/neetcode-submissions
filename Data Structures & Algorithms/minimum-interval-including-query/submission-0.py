import heapq

class Solution:
    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        # 1. Sort intervals by start
        intervals.sort(key=lambda x: x[0])

        # 2. Sort queries
        sorted_queries = sorted(queries)

        # 3. Initialize
        heap = []      # (length, end)
        answers = {}   # query -> min interval length
        i = 0          # Pointer for intervals

        # 4. Process queries
        for q in sorted_queries:

            # TODO 1: Push all intervals whose start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]

                # Calculate length
                # Push (length, end) into heap
                length = end - start + 1
                heapq.heappush(heap, (length, end))

                i += 1

            # TODO 2: Remove expired intervals
            # Keep popping while heap top's end < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # TODO 3: Record answer
            # If heap is not empty, use its minimum length
            # Otherwise, answer is -1
            if heap:
                answers[q] = heap[0][0]
            else:
                answers[q] = -1

        # 5. Restore original query order
        return [answers[q] for q in queries]
        