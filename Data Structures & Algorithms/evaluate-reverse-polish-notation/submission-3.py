class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        o_list = ['+', '-', '*', '/']
        for t in tokens:
            if t in o_list:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    r = first + second
                elif t == "-":
                    r = first - second
                elif t == "*":
                    r = first * second
                else:
                    r = int(first / second)
                stack.append(r)
            else:
                stack.append(t)

        result = int(stack.pop())
        return result