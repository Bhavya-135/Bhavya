def postfixvaluation(s):
    st=[]
    s=s.split()
    print(s)
    print(len(s))
    for i in range(len(s)):
        if s[i].isdigit():
            st.append(int(s[i]))
        elif s[i]=='+':
            a=st.pop()
            b=st.pop()
            st.append(b+a)
        elif s[i]=='-':
            a=st.pop()
            b=st.pop()
            st.append(b-a)
        elif s[i]=='*':
            a=st.pop()
            b=st.pop()
            st.append(b*a)
        elif s[i]=='/':
            a=st.pop()
            b=st.pop()
            st.append(b/a)
    return st.pop()
s='10 2 8 * + 3 -'
val=postfixvaluation(s)
print(val)