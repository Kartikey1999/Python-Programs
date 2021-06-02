l1=[1,5,6,9,11]
l2=[3,4,7]

size_one=len(l1)
size_two=len(l2)

res=[]
i,j=0,0
while i<size_one and j<size_two:
    if l1[i]<l2[j]:
        res.append(l1[i])
        i+=1

    else:
        res.append(l2[j])
        j+=1

res=res+l1[i:]+l2[j:]
print(str(res))





