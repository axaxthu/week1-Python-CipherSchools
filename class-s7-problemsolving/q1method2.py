#another method to do question 1
n=int(input())
for i in range(n):
    for j in range(n):
        print(max(max(i,j),max(n-j-1,n-i-1)),end=" ")
    print()    