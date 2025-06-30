class queue:
    def __init__(self,dataval):
        self.dataval=dataval
        self.next=None

class dynamic:
    def __init__(self):
        self.front=None

    def enque(self,newdata):
        newnode=queue(newdata)
        if self.front is None:
            self.front=newnode
        last=self.front
        while(last.next):
            last=last.next
        last.next=newnode

    def deque(self):
        if self.front is None:
            print('empty')
        else:
            x=self.front.dataval
            self.front=self.front.next
            return x
    
    def display(self):
        if self.front is None:
            print('empty')
        else:
            temp=self.front
            while(temp):
                print(temp.dataval,end=' ')
                temp=temp.next
            print()
s1=dynamic()
s1.front=queue(10)
s1.enque(20)
s1.enque(30)
s1.enque(40)
s1.enque(50)
s1.display()
s1.deque()
s1.display()
s1.deque()
s1.display()
s1.deque()
s1.display()