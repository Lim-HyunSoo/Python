# https://www.acmicpc.net/problem/17269

N, M = map(int, input().split())

A, B = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2 ,1, 1, 1, 2, 2, 1]

name = ''

if(M < N):
    for i in range(M):
        name += B[i] + A[i] 
    name += A[M:len(A)]

else:
    for i in range(N):
        name += A[i] + B[i]
    name += B[N:len(B)]
  
lst = [alp[ord(i) - ord('A')] for i in name]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
        
print("{}%".format(lst[0] % 10*10 + lst[1]%10))
