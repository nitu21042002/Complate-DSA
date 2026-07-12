#Write a program to demonstrate shallow copy of a nested list.
lst1=[1,2,3,4,[4,5,6],7]
lst2=lst1.copy()  #shallow copy of lst1

lst1[0]=0 #change in liner list modify only original list not coped list due to 
         #shallow copy shallow copy allow to change only nested list not liner list
print("lst1:",lst1)
lst1[4][0]=0 #change in both list modifyed original and coped list  due to 
         #shallow copy shallow copy allow to change only nested list
print("lst2:",lst2)

lst2[1]=9 #modify both list because changing  in liner list
print("lst2:",lst2)
lst2[4][2]=10 #modify only lst2 list because changing  in nested list
print("lst2:",lst2)