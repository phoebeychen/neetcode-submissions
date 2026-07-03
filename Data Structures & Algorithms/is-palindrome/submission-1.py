class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse string
        # letter, digits -> isalnum()
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    #  O(n)
    #  O(n)