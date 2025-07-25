class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval,end=' ')
            printval=printval.nextval
        print()

    def atbeg(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
        newnode.nextval=self.headval
        self.headval=newnode

    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
        last=self.headval
        while(last.nextval):
            last=last.nextval
        last.nextval=newnode

    def atmid(self,middle,newdata):
        if middle is None:
            print('data not present')
        temp=self.headval
        newnode=node(newdata)
        while(temp.dataval!=middle and temp.nextval!=None):
            temp=temp.nextval
        newnode.nextval=temp.nextval
        temp.nextval=newnode

    def removenode(self,removekey):
        headval=self.headval
        if(headval is not None):
            if(headval.dataval==removekey):
                self.headval=headval.nextval
                headval=None
                return
        while(headval is not None):
            if(headval.dataval==removekey):
                break
            prev=headval
            headval=headval.nextval
        if (headval==None):
            return
        prev.nextval=headval.nextval
        headval=None

s1=slinkedlist()
s1.headval=node('mon')
e2=node('tue')
e3=node('wed')
s1.headval.nextval=e2
e2.nextval=e3
s1.listprint()
s1.atbeg('sun')
s1.listprint() 
s1.atend('thu')
s1.listprint()
s1.atmid('tue','fri')
#list1.inbetween(list1.headval,"fri")
s1.listprint()
s1.removenode('sat')
s1.listprint()
