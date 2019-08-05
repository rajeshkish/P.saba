#S
k9,m9=map(int,input().split())
m9k9=list(map(int,input().split()))
l1=[]
for i in range(0,m9):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(m):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(m9k9[lower-1:upper])
     print(x)
