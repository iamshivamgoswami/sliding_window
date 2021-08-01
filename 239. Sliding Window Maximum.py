import collections
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        i = j = 0
        n = len(a)
        ans = []
        l = collections.deque()
        while j < n:

            while len(l) > 0 and l[-1] < a[j]:
                l.pop()
            l.append(a[j])

            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans.append(l[0])
                if len(l) > 0 and a[i] == l[0]:
                    l.popleft()

                i += 1
                j += 1
        return ans