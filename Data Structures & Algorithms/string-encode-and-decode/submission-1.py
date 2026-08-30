class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result += str(len(strs[i]))
            result += "#"
            result += strs[i]
        return result

    def decode(self, s: str) -> List[str]:
        result_list = []
        if s == "":
            return []
        else:
            p = 0
            while p < len(s):
                i = p
                while (s[i] != "#"):
                    i += 1
                length = int(s[p:i])
                ss = s[i+1:i+1+length]
                result_list.append(ss)
                p = i+1+length
            return result_list
