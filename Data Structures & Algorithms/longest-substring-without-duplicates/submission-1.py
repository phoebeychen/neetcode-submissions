class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
            cnt = max(cnt, len(seen))
        return cnt

                
