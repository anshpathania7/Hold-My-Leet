class Solution:
    
    def getReversedNum(self,num: int)->int:
        reversed_num=0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num
    
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            return x==self.getReversedNum(x)
            
        