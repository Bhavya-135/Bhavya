#dynamic implementation of stack(creating data stucture using linked list)
class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class dynamic:
    def __init__(self):
        self.top=None
    def listprint(self):
        printval=self.top
        while printval is not None:
            print(printval.dataval,end=' ')
            printval=printval.nextval
        print()
    def push(self,newdata):
        newnode=node(newdata)
        if self.top is None:
            self.top=newnode
        newnode.nextval=self.top
        self.top=newnode
    def pop(self,removekey):
        top=self.top
        if(top is not None):
            if(top.dataval==removekey):
                self.top=top.nextval
                top=None
                return


s1=dynamic()
s1.top=node(10)
s1.push(20)
s1.listprint()
s1.push(30)
s1.listprint()
s1.push(40)
s1.listprint()
s1.pop(40)
s1.listprint()
s1.pop(30)
s1.listprint()
s1.pop(20)
s1.listprint()
s1.p(10)
s1.listprint()