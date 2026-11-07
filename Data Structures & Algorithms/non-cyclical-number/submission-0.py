class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def get_next(n):
            total = 0

            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10

            return total

        while n != 1:
            n = get_next(n)
            if n in visited:
                return False
            else:
                visited.add(n)
        
        return True