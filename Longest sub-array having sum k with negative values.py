class Solution:
    def maxSubArrayLen(self, l: List[int], k: int) -> int:
        d = {}
        summ = 0
        maxx = 0
        for i in range(len(l)):
            summ += l[i]
            if summ == k:
                maxx = i + 1
            elif summ - k in d:
                maxx = max(i - d[summ - k], maxx)
            if summ not in d:
                d[summ] = i

        return maxx
