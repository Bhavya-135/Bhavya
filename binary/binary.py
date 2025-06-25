#decimal to binary
n=int(input())
x=bin(n)
print(x)
print(type(x))
x=x[2:]
print(x)
da=int(x,2)
print(da)

#decimal to octal
n=int(input())
x=oct(n)
print(x)
print(type(x))
x=x[2:]
print(x)
da=int(x,8)
print(da)

#decimal to hexadecimal
n=int(input())
x=hex(n)
print(x)
print(type(x))
x=x[2:]
print(x)
da=int(x,16)
print(da)


