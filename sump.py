ls=[]
l=0
a, b=[int(l)for l in input().split()]
for i in range(a):
  t=int(input())
  ls.append(t)
for i in range(0,b):
  k=int(ls[i])
  l=l+k
print(l)
