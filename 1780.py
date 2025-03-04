class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans=''
        while n>0:
            d=n%3
            ans=str(d)+ans
            n//=3
        for i in ans:
            if int(i)>1:return False
        return True