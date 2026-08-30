class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for i in range(len(strs)):
            si = "".join(sorted(strs[i]))
            if si not in mapping:
                mapping[si] = []
                mapping[si].append(strs[i])
            else:
                mapping[si].append(strs[i])
        r_list = []
        for key, value in mapping.items():
            r_list.append(value)
        return r_list
        