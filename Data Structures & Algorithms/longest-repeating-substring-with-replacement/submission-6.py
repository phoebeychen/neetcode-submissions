class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        seen = defaultdict(int)
        maxC = 0 #  max(maxC, seen[s[r]]), window - maxC <= k
        
        for r in range(len(s)):
            seen[s[r]] += 1
            maxC = max(maxC, seen[s[r]])
            while r - l + 1 - maxC > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            
        return res


            



