# https://www.acmicpc.net/problem/15969

n = int(input())

scores = list(map(int, input().split()))

maxS = 0
minS = scores[0] 

for i in scores:
    if(i > maxS):
        maxS = i
    
    if(i < minS):
        minS = i
        
print(maxS - minS)
