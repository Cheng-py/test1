class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        a=x
        if (a[::-1]==x):
            print(True)
        else:
            print(False)

solution = Solution()
a=121
solution.isPalindrome(a)

print('test1')