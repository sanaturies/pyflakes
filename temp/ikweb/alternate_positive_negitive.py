
# given a list of pos and neg ints, rearrage the elements so that the positive and negitive numbers alternate. Order of the pos elems 
# should be preserved, same with the negitive ones.
# 0 is pos. 
# start with pos
# any extras appear at end of output.

lst=[-1,3,-2]
pos=[]
neg=[]
new=[]
for i in lst:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

for i in range((len(pos)+len(neg))//2):
    print(i)
    if len(pos)>0:
        new.append(pos[0])
        pos.pop(0)
    if len(neg)>0:
        new.append(neg[0])
        neg.pop(0)
    print(new)

if len(pos)>=1:
    new.append(pos)
elif len(neg)>=1:
    new.append(neg)
print(new) 