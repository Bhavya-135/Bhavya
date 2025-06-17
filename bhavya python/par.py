guest_list=[]
print("Welcome to party project")
while(True):
    print("1.enter 1 to add a guest")
    print("2. enter 2 to remove a guest who cancles")
    print("3.enter 3 to check if a friend is on the list or not")
    print("4.enter 4 to sort and print the final guest list ")
    print("5.enter 5 to exit")
    c=int(input("Welcome to the party project"))
    if(c>=1 and c<=5):
        if(c==1):
            n=input("enter the quest name:")
            guest_list.append(n)
            print(f"{n} is added to the quest list'!")
        elif(c==2):
            cn=input("enter the name of the guest who cancelled")
            if cn in guest_list:
                guest_list.remove(cn)
                print(f"{cn}is removed from the guest list!.....")
            else:
                print(f"{cn} is not present in the quest list....!")
        elif(c==3):
            c_g=input("enter the guest name: ")
            if c_g in guest_list:
                print(f"{c_g} is atttending the party.!")
            else:
                print(f"{c_g}is not atttending the party...!")
        elif(c==4):
            guest_list.sor()
            print("Here's the finailized list of guest's who are atttending the part....!")
            print(guest_list)
        
    else:
           print("Enter the party.......!") 