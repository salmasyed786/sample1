ar = [2,1,5,4]
ar.sort()
j=1
for i in range(0,len(ar)-1):  
    if ar[i] == j:         
        j+=1
    else:
                #print(j)      
        print(j)
        j+=1