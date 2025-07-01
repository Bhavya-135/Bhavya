class customer:
    def __init__(self,name,no_of_items):
            self.name = name
            self.no_of_items = no_of_items                    # intialized the method 

    def calcualtion(self):                                        #calculation as a method
        x = self.no_of_items
        total = 0
        for i in range(x):
            p = int(input())
            total += p
        return total

s1 = customer("farheen",4)
total=s1.calcualtion()
if (total>200):
      print(total -total*0.2)
else:
      print(total) 


# or
class customer:
    def __init__(self,name,no_of_items):
            self.name = name
            self.no_of_items = no_of_items                    # intialized the method 

    def calcualtion(self):                                        #calculation as a method
        x = self.no_of_items
        total = 0
        for i in range(x):
            p = int(input())
            total += p
        return total
    
name = input()
no_of_items = int(input())
c1 = customer(name,no_of_items)
total=s1.calcualtion()
if (total>200):
      print(total -total*0.2)
else:
      print(total) 