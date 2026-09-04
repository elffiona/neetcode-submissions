class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        result = []

        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))

            if right >= k - 1:
                left = right - k + 1

                while heap[0][1] < left:
                    heapq.heappop(heap)

                result.append(-heap[0][0])

        return result
         