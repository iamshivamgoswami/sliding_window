s="abaccab"
i=j=0
n=len(s)
k=2
d={}
maxx=0
while j<n:
    if s[j] not in d:
        d[s[j]]=1
    else:
        d[s[j]]+=1
    if len(d)<k:
        j+=1
    elif len(d)==k:
        maxx=max(j-i+1,maxx)
        j+=1
    elif len(d)>k:
        while len(d)>k:
            d[s[i]]-=1
            if d[s[i]]==0:
                del d[s[i]]
            i+=1
        j+=1
print(maxx)