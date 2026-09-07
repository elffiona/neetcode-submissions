class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1

        while lower < upper:
            mid = lower + (upper - lower) // 2
            time = sum([(p + mid - 1) // mid for p in piles])
            if time > h:
                lower = mid + 1
            else:
                upper = mid
        
        return upper