## Given a number N, print its factors.
## Input Size : n<=1000
## Sample Testcase :
## INPUT
## 6
## OUTPUT
## 1 2 3 6

n = int(input())
k = []
for i in range(1,n+1):
    if n%i ==0:
        k.append(i)
print(" ".join(map(str,k)))
