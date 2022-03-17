class Solution:
    def intToRoman(self, num: int) -> str:
        l=[1,5 ,10, 50, 100, 500, 1000]
        l1=["I","V" ,"X", "L", "C", "D","M"]
        l2=["X", "C" ,"M"]
        l3=["V","L", "D"]
        s=""
        i = 6
        while num!=0:
            if num >= l[i]:
                s+=l1[i]
                num = num - l[i]
            elif num >= 9/10 * l[i] and l1[i] in l2 :
                s+=l1[i-2]+l1[i]
                num = num - 9/10 * l[i]
                i-=1
            elif num >= 8/10 * l[i] and l1[i] in l3:
                s+=l1[i-1]+l1[i]
                num= num - 8/10 * l[i]
                i-=1
            else:
                i-=1
        return s
