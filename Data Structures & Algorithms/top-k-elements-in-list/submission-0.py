class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]] += 1
            else:
                mapping[nums[i]] = 0
                mapping[nums[i]] += 1
        sorted_mapping = dict(sorted(mapping.items(), key=lambda x: x[1], reverse=True))
        result = []
        keys = list(sorted_mapping.keys())
        for j in range(k):
            result.append(keys[j])
        return result