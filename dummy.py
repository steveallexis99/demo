l=[222,37,97,1,123,11,9,79,97,1,5]
for i in range(len(l)):
    j=i-1
    m=i
    for j in range(i,len(l)):
        if l[m]>l[j]:m=j
    l[m],l[i]=l[i],l[m]
print(l)