class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones, s1 - s2)

        if not stones:
            return 0

        return -stones[0]
