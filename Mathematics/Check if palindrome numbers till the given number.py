## Simi is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.Simi has told you about this and want your help. You design an algorithm in order to help simi.

## Input Description:
## You will be given a number ānā

## Output Description:
## Print the count of all palindromic numbers till ānā(inclusive)

## Sample Input :
## 5
## Sample Output :
## 5

n = int(input())
count = 0
for i in range(1,n+1):
    b = str(i)
    if (b == b[-1::-1]):
        count = count + 1
print(count)
