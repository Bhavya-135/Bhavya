ipl_list=["csk","rcb","mi","srh","gt","pbks"]
print("Accesing the elements without index:")
for i in ipl_list:
    print(i)
print("Accesing the elements with index:")
for i in range(len(ipl_list)):
    print(ipl_list[i])

del ipl_list[1]
print(ipl_list)
del ipl_list[4]
print(ipl_list)
