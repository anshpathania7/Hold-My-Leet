class Solution:
    
    def reverse(self, x: int) -> int:
        rev = int("".join(reversed(list(str(abs(x))))))
        if x<0:
            rev*=-1
        return rev if (rev>= -2**31 and rev <= 2**31) else 0