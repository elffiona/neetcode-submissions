class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = [False, False, False]

        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                # Can not be used
                continue
            else:
                if tri[0] == target[0]:
                    matched[0] = True

                if tri[1] == target[1]:
                    matched[1] = True

                if tri[2] == target[2]:
                    matched[2] = True
                
        return matched == [True, True, True]