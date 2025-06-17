
food_list=["panipuri","choco","mango","dahipuri","masalavada","malaipuri","hydbiryani"]
tuple=(10,20,30,40,60,100)
food_length=len(food_list)
for i in range(food_length):
    n=input("enter a name of food item: ").lower()
    m=int(input("enter the quantity of food item: "))
    if n==food_list[i].lower():
        print(f"{n} is in the list....!")
    else:
        print(f"{n} does not match {food_list[i]}")
    