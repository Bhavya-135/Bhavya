santa_list=[]
print("welcome to the Christmas GIFs")
while(True):
    print("***************MENU***************")
    print("1.enter 1 to add a gifts")
    print("2. enter 2 to remove a duplicates")
    print("3.enter 3 to check the final list")
    gift_list=int(input("Enter the toy list: "))

    u=["toy","barbe","cat","scale","choco","cake"]
    list=[]
    for i in range(gift_list):
        Temp=int(input(f"Enter the integer value at {i} position"))
        list.append(Temp)
    print(f"User entered list : {list}")
    for i in list:
        if i  not in u:
            u.append(i)
    print(f"unique list ",u)
