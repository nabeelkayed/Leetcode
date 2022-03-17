class Solution:
    def reverse(self, x: int) -> int:
        b=""
        if not(-2**31 <= x and x <= 2**31 - 1):
            return "0"
        if (x < 0):
            b+="-"
            x=-x
        elif x==0:
            return "0"
            
        while x > 0 :
            a = x % 10
            x = x // 10
            if a != 0 :
                b= b + str(a)
            elif b != "" and b!="-":
                b+="0"
        if not(-2**31 <= int(b) and int(b) <= 2**31 - 1):
            return "0"
        
        return b
