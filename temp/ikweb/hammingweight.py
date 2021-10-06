
#find hamming weight of an array of integers

lst=[4,2,3]
lstlst=[[],[],[]]
for i in range(len(lst)):
    x=lst[i]
    while x!=1 or x!=0:
        while x!=1 or x!=0:
           y%=2
           x/=2

        lstlst[i].append(lst[i])
        if lst[i]==1 or lst[i]==0:
            break
print(lst)
