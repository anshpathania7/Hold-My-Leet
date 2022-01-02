class Solution:  
    def isPalindrome(self, l,r,s):
        #print("checkking for => ",s[l:r])
        mid = l + (r-l)//2
        for i in range(l, mid):
            if s[l]!=s[r-1]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        x,y=0,0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if r-l-1> y-x:
                x,y=l+1,r-1
            l,r=i-1,i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if r-l-1> y-x:
                x,y=l+1,r-1
        return s[x:y+1]