
#high to low 
def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1 
        rlh(x,y)


a,b=map(int,input().split())
rlh(a,b)#calling function

#low to high
def rlh(x,y):
    if(x>=y):
        print(x)
        x-=1 
        rlh(x,y)


a,b=map(int,input().split())
rlh(a,b)#calling function

#factorial using r


def fac(n):
    p = 1
    for i in range(1, n+1):
        p *= i
        print(p)

n = int(input())
fac(n)
#reccc 


def fac(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fac(n-1)#recursive calling

n = int(input())
f=fac(n)
print(f)
#5 to 1

def fac(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

n = int(input())
f = fac(n)
print(f)
#now
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

n = int(input())
print(fac(n))


#new
def rgcd(a,b):
    if(a==b):
        return a 
    if (a>b):
        return rgcd(a-b,b)
    else:
        return rgcd(b,b-a)
a,b=map(int,input().split())
ans=rgcd(a,b)
print(ans)
