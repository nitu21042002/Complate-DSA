#Write a program to demonstrate nested list references.

#this is a normal copy both lst and lst2 are created in same memory loction that's why chanig in a one 
# list affect other also both have same id 
lst=[[1,2,3,4],[5,6,7,8]]
lst2=lst

lst2[0][1]=9
print(lst)
print(lst2)

lst[0][3]=10

print(lst)
print(lst2)
print(id(lst))
print(id(lst2))

#this is shallow copy it means both lst3 and lst4 are shearing same memory loction but in olny liner list both have
#  different memory loction for nested list if changing in one list in liner loction affect both list but if chang in 
# nested in one list does not affet other one
 
lst3=[1,2,3,[1,2,3,4],[5,6,7,8],9,0]
lst4=lst3

lst4[0]=9
print(lst3)
print(lst4)

lst3[3][3]=10

print(lst3)
print(lst4)
print(id(lst3))
print(id(lst4))



#this is deep copy it means both lst5 and lst6 having different memory loction for liner and nested list
# if changing in one list in liner loction can not affect both list and also if chang in 
# nested in one list does not affet other one
import copy
lst5=[1,2,3,[1,2,3,4],[5,6,7,8],9,0]
lst6=copy.deepcopy(lst5)

lst6[0]=9
print(lst5)
print(lst6)

lst5[3][3]=10

print(lst5)
print(lst6)
print(id(lst5))
print(id(lst6))