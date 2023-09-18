#sort 0's 1's 2's

arr=[0,1,2,2,0]

l,m,r=0,0,len(arr)-1

while m<r:
    
    if arr[m]==0:
        arr[l],arr[m]=arr[m],arr[l]
        l+=1
        m+=1
        
    elif arr[m]==1:
        m+=1

        
    else:
        arr[r],arr[m]=arr[m],arr[r]
        r-=1
        
