class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        seen = defaultdict(int)
        maxC = 0 #  max(maxC, seen[s[r]]), window - maxC <= k
        
        for r in range(len(s)):
            seen[s[r]] += 1 # 每次r循环seen都+1,保持记录
            maxC = max(maxC, seen[s[r]]) # maxC只记seen里面更多的那个

            while (r - l + 1) - maxC > k: # 循环停止的条件, r - l + 1 窗口需要动态计算
                seen[s[l]] -= 1 # 不合法的时候缩小左窗口变合法
                l += 1

            res = max(res, r-l+1)
            
        return res


            



