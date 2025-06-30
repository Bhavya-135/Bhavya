class queue:
    def __init__(self,dataval):
        self.dataval=dataval
        self.next=None

class dynamic:
    def __init__(self):
        self.front=None
        self.rear=None

    def enque(self,newdata):
        newnode=queue(newdata)
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
            newnode.next=self.front

    def deque(self):
        if self.front is None:
            print('empty')
        elif self.front==self.rear:
            x=self.front.dataval
            self.front.dataval=0
            self.front=None
            self.rear=None
        else:
            x=self.front.dataval
            self.front.dataval=""
            self.front=self.front.next
            return x
    
    def display(self):
        if self.front is None:
            print('empty')
        temp=self.front
        while(temp):
            print(temp.dataval,end=' ')
            temp=temp.next
            if(temp==self.front):
                break
        print()
q1=dynamic()
while True:
    print("enque <value>")
    print("deque")
    print("display")
    print("quit")
    do = input("what would u like to do? ").split()

    operation = do[0].strip().lower()
    if operation == 'enque':
        q1.enque(int(do[1]))
    elif operation == 'deque':
        popped = q1.deque()
        if popped is None:
            print("queue is empty")
        else:
            print("popped value: ",int(popped))
    elif operation == "display":
        q1.display()
    elif operation == "quit":
        break