class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1 = i + j      # increment
                p2 = i + j + 1  # original
                total = int(num1[i]) * int(num2[j]) + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        answer = "".join(str(d) for d in result)
        answer = answer.lstrip("0")
        if answer == "":
            answer = "0"
        
        return answer

