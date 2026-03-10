class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=ans=0
        for i, c in enumerate(s):
            if c in "aeiou":
                vowels+=1
            left = i-k+1
            if left <0:
                continue
            ans=max(vowels,ans)
            if s[left] in "aeiou":
                vowels-=1
        return ans