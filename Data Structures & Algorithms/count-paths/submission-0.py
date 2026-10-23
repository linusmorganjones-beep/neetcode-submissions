class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        move_number = m + n - 2
        choose_lower = min(m-1, n-1)

        def factorial(l:int):
            factorial = 1
            for i in range(1, l + 1):
                factorial = factorial * i
            return factorial
        
        return int(factorial(move_number) / (factorial(choose_lower) * factorial(move_number - choose_lower)))