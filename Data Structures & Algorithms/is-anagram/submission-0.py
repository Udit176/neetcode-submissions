class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(nlogn) solution#
        '''if sorted(s) == sorted(t):
            return True
        return False'''

        #O(n) solution
        from collections import Counter
        return Counter(s) == Counter(t)

       



