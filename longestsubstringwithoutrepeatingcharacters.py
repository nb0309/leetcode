class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        max=0
        for i in range(0,len(s)):
            
            j=i
            while j<len(s) and s[j] not in l:
                l.append(s[j])
                j+=1
            
            if max<len(l):
                max=len(l)
            l.clear()
        return max
s=Solution()
ss="pwwkew"
val=s.lengthOfLongestSubstring(ss)
print(val)
