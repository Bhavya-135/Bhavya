# single circular linked list
# no node is null , the last node points to the first node.
class node:                                       #NODE CREATION 
    def  __init__(self,dataval):
        self.dataval = dataval                     #DATA
        self.nextval= None                            #ADDRESS

class sclinkedlist:
    def __init__(self):
        self.headval = None                          #initailly head value

# beginning of insertion:
    def listprint(self):
        printval = self.headval                       #head node address 1000 starting 
        while printval is not None:
            print(printval.dataval,end=" ")           # 1000 data = 1          
            printval = printval.nextval             # 2000,3000/.. # 2000 is equal to 3000 (next data address we have to check untill it is equal to stat to end node 1000 = 1000)
            if(printval==self.headval):              #printval = 2000 headval(evary time) = 1000 1st case # startinh is head nood and endinh is also head node is last
                break
        print()

# starting

    def atstart(self,newdata):
        newnode = node(newdata)                 # we dont have the list so we created the new node
        if(self.headval is None):            # the lis empty not present in this condition
            newnode.nextval = newnode                  # none first staring  we will add the 1000 in none place 
            self.headval = newnode
        else:
            newnode.nextval = self.headval         #new node lo unna none tisi 1000 value add ayidhi in (newnode address)
            self.headval=newnode                   # aa vachina new node ipudu headnode ayidhi 
    
    def atend (self,newdata):
        newnode = node(newdata)          #create node and stored in  node
        if self.headval is None:
            newnode.nextval = newnode
            self.headval= newnode
        else:
            temp = self.headval       #temp = 1000
            while(temp.nextval):       # 2000 = temnp.nextvale
                temp = temp.nextval
                if(temp == self.headval):    # 1000 = 1000 and taht 100 is stored in temp in temp we have last node value
                    break
            temp.nextval = newnode            # temp.newval = 1000 = 5000
            newnode.nextval = self.headval  
            #at end 
    def inmid(self,middle,newdata):
        newnode = node(newdata)
        if middle is None:
            print("data not present")
            return
        else:
            temp=self.headval         
            while (temp.dataval!=middle and temp.nextval!=self.headval): 
                temp = temp.nextval                       
            newnode.nextval = temp.nextval
            temp.nextval=newnode 
            
    def removenode(self,removekey):
        temp=self.headval
        if(temp is not None):
            if(temp.dataval==removekey):
                del self.headval
                temp=temp.nextval
                self.headval=temp
                return
        while(temp is not None):
            if(temp.dataval==removekey):
                break
            if(temp.nextval==self.headval):
                break
            prev=temp
            temp=temp.nextval
        if (temp==self.headval):
            return
        prev.nextval=temp.nextval
        temp=None

s1=sclinkedlist()
s1.headval=node('mon')
s1.atstart('sun')
s1.listprint() 
s1.atend('thu')
s1.listprint()
s1.inmid('tue','fri')
s1.listprint()
s1.removenode('sun')
s1.listprint()