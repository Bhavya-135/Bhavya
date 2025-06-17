A=input("enter the name")
v=""
for char in A:
    if char.isalpha():
        v+=char
if v.isalpha():
    print("valid")
else:
    print("Not valid")
