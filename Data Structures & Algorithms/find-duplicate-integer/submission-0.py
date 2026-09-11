class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mm = set()
        for n in nums:
            if n in mm:
                return n
            else:
                mm.add(n)