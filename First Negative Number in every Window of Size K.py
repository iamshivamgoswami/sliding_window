import collections


def printFirstNegativeInteger(a, n, k):

    i = j = 0
    l = collections.deque()
    ans = []
    while j < n:
        if a[j] < 0:
            l.append(a[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:

            if len(l) == 0:
                ans.append(0)
            if len(l) > 0:
                ans.append(l[0])
            j += 1
            if l and a[i] == l[0]:
                l.popleft()
            i += 1

    return (ans)