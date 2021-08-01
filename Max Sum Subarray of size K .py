class Solution:
    def maximumSumSubarray (self,k,arr,n):
        i=j=0
        summ=maxx=0
        while j<n:
            summ+=arr[j]

            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                maxx=max(summ,maxx)
                summ-=arr[i]
                j+=1
                i+=1
        return maxx


