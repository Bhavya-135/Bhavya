operators=(["+","-","*","/","(",")","^"])
priority={"+":1,"-":1,"*":2,"/":2,"^":3}


def infix_to_postfix(expression):#input expression
    stack=[] 
    output=""
    for i in expression:
        if i not in operators:
            output+=i
        elif i=="(":
            stack.append("(")
        elif i==")":
            while stack and stack[-1]!="(":
                output+=stack.pop
        else:
            while stack and stack[-1]!="(" and priority[i]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(i)
    while stack:
        output+=stack.pop()
    return output
expression=input("enter infix expression:  ")
print("infix expression : ",expression)
print("postfix expression: ",infix_to_postfix( expression))