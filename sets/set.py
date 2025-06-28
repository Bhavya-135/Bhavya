set={'python','java','c','c++','Angular js','Node js','Sql'}
print(set)
print(type(set))
#accessing set items
print('Sql' in set)
#adding elements
set.add('m')
print(set)
set.add('js')
print(set)
set.add('express js')
print(set)
#update
set.update(['R','g'])
print(set)
#removing itmes from set
set.remove('R')
print(set)

#discard and pop methods
set.pop()
print(set)

set.discard('c')
print(set)


#clear
set.clear()
print(set)

#union
set1={1,2,3}
set2={3,4,5}
print(set1|set2)

#intersection

set4={1,2,3}
set5={2,3,5}
print(set4&set5)
#differences
set6={6,7,8}
set7={9,10,11}
dm=set6.difference(set7)
print('DIfferences:',dm)
print()

#issubset
isub=set6.issubset(set7)
print("issubset: ",(isub))
print()

#issuperset()
sub=set6.issuperset(set2)
print(sub)