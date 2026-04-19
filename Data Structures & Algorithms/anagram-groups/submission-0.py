class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            current = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    current.append(strs[j])
                    used[j] = True

            res.append(current)

        return res


          
      

        