A=int(input())
for i in range(A):
    for j in range(A-1,i,-1):
        print(" ",end="")
    print(chr(65+i),end="")
    for j in range(2*i-1):
        print(" ",end="")
    if i!=0:
        print(chr(65+i),end="")
    for j in range((A-i-1)*2+1):
        print(" ",end="")
    print(chr(65+i),end="")
    for j in range(2*i-1):
        print(" ",end="")
    if i!=0:
        print(chr(65+i),end="")
    print()
    
