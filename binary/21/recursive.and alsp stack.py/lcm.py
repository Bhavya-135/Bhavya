#lcm using recursion
#new
def rgcd(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if (a>b):
        return rgcd(a-b,b,x,y)
    else:
        return rgcd(b,b-a,x,y)
a,b=map(int,input().split())
ans=rgcd(a,b,a,b)
print(ans)
