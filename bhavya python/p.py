str=input("enter the name")
d_o=0
v_c=0
s_c=0
for char in str.lower():
    if char.isdigit():
        d_c+=1
    elif char.isalpha():
        if char in ['a','e','i','o','u']:
            v_c+=1
    else:
        s_c+=1 
print(f'Digit count: {d_o}')
print(f'vowel count: {v_c}')
print(f'speacail count: {s_c}')