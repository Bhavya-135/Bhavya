def postfixevaluation(s):
    st=[]
    s=s.split()
    print(s)
    print(len(s))
    for i in range(len(s)):
        if s[i].isdigit():
            st.append(int(s[i]))
        elif s[i]=="+":
            a=st.pop()
            b=st.pop()
            st.append(b+a)
        elif s[i]=="-":
            a=st.pop()
            b=st.pop()
            st.append(b-a)
        elif s[i]=="*":
            a=st.pop()
            b=st.pop()
            st.append(b*a)
        elif s[i]=="/":
            a=st.pop()
            b=st.pop()
            st.append(b/a)
    return st.pop()


s="111 222 844 * +++ 3 -"
val=postfixevaluation(s)
print(val)