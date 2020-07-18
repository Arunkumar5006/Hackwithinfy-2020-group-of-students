def maxdiff(lis):
    i=0
    j=len(lis)-1
    lis.sort()
    summ=0
    while i<j:
        summ+=lis[j]-lis[i]
        i+=1
        j-=1
    return summ
n=int(input())
lis=[]
for _ in range(n):
    lis.append(int(input()))
print(maxdiff(lis))
