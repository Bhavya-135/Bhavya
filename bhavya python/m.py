str=input("enter the string name")
c_upper=0 
c_lower=0
con_c=0

for char in str:
    if str.isalpha():
        if char in ['A','E','I','O','U']:
            c_upper+=1
        elif char in ['a','e','i','o','u']:
            c_lower+=1
        else:
            con_c+=1
print(f'upper count: {c_upper}')
print(f'lower count: {c_lower}')
print(f'con count: {con_c}')