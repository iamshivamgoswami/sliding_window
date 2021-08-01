import collections

s="ADOBECODEBANC"
t="ABC"
def func(s,t):

    if not t or not s:
        return ""
    d=collections.Counter(t)
    required=len(d)
    l=r=0
    formed=0
    window_count={}
    ans=float("inf"),None,None
    while r<len(s):
        character=s[r]
        window_count[character]=window_count.get(character,0)+1
        if character in d and window_count[character]==d[character]:
            formed+=1
        while l<=r and formed==required:
            character=s[l]
            if r-l+1<ans[0]:
                ans=(r-l+1,l,r)
            window_count[character]-=1
            if character in d and window_count[character]<d[character]:
                formed-=1
            l+=1
        r+=1
    return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]

print(func(s,t))