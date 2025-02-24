# Time O(n + n log n)
# Space O(n)
class Solution:
    def expand(self, s: str) -> List[str]:
        return self.dfs(s, 0)

    def dfs(self, s: str, i: int) -> List[str]:
        if i == len(s) - 1: return [s[i]]
        if i > len(s) - 1: return []

        #left
        res = []
        if s[i] == '{':
            options = []

            j = i+1
            while s[j] != '}':
                if s[j] != ',':
                    options.append(s[j])
                j += 1
            options.sort() # O(n log n)
            #call right dfs
            result = self.dfs(s, j + 1)
            if len(result) > 0:
                for option in options:
                    for k in range(len(result)):
                        res.append(option + result[k])
                return res
            else: return options

        #right
        else:
            result = self.dfs(s, i + 1)
            for k in range(len(result)):
                    res.append(s[i] + result[k])
            return res
        