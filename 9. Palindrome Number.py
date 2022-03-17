class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i=len(x) - 1
        result = True
        for j in range(len(x)):
            if x[i]==x[j]:
                i=i-1
                if (i==j-1 or i==j-1):
                    break
                continue
            result=False
        return result
                
