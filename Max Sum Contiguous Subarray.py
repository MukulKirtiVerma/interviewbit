class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        a=A
        if(max(a)<0):return max(a)
        else:
            i=0
            while(a[i]<0):i+=1
            mx,j,temp=a[i],i,a[i]
            i+=1
            while(i<len(a)):
                if(i+2<len(a) and temp+a[i]<0):
                    i+=1
                    while(i<len(a) and a[i]<0):
                        i+=1
                    j=i
                    try:
                       temp=a[j]
                       if(mx<temp):
                           mx=temp
                    except:
                        pass
                    i+=1
                    
                    continue
                
                temp=temp+a[i]
                #print(a[j:i+1],temp,mx)
                if(mx<temp):
                    mx=temp
                i+=1
            return mx
