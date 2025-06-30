def toh(n,a,b,c):
    if(n>0):
        toh(n-1,a,c,b)
        print(a,'->',c)
        toh(n-1,b,c,a)
n=int(input())
toh(n,'a','b','c')