class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove alphanumeric values, then convert to lowercase
        s = ''.join(filter(str.isalnum, s)).lower() 
        return s[::] == s[::-1]

        #Time: O(n)
        #Space: O(n)
        