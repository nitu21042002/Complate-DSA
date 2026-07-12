#Write a program to demonstrate shallow copy of a list.
lst1=[1,2,3,4,5,6,8,9,7]
lst2=lst1.copy()  #shallow copy of lst1

lst1[0]=0 #change in liner list modify original list        
print("lst1:",lst1)
lst1[4]=10 #modify original list
print("lst1:",lst1)

lst2[1]=9 #modify copied list 
print("lst2:",lst2)
lst2[2]=10 #modify copied list
print("lst2:",lst2)