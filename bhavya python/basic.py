a=int(input("Enter a int Number"))
b=float(input("Enter float Number"))
c=input("string name")
print("Before converstion")

#int 
k=str(a)
print("After conversion of int t0 string",k)
h=float(a)
print("After conversion of int to float",h)
m=complex(a)
print("After conversion of int to complx",m)


#float
o=str(b)
print("After conversion of float to string",o)
l=int(b)
print("After conversion of float t0 int",l)
n=complex(b)
print("After conversion of float t0 complex",n)


#string 
j=int(c)
print("After conversion of string t0 int",j)
i=float(c)
print("After conversion of string t0 float",i)
g=list(c)
print("After conversion of string t0 list",g)
t=tuple(c)
print("After conversion of string t0 tuple",t)
print("After converstion")