class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        j = i = 0
        maxx = 0
        d = {}
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1

            if len(d) < k:
                maxx = max(j - i + 1, maxx)
                j += 1
            elif len(d) == k:

                maxx = max(j - i + 1, maxx)
                j += 1
            else:
                while len(d) > k:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i += 1
                j += 1
        return maxx

