#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        c=0
        for i in range(k):
            if s[i] in vowels:
                c+=1
        currents=s[:k]
        maxvalue=c
        if c==k:
            return c
        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
                if currents[0] in vowels:
                    c-=1
            else:
                if currents[0] in vowels:
                    c-=1
            currents=currents[1:]
            currents+=s[i]
            if c>maxvalue:
                maxvalue=c
        return maxvalue


        