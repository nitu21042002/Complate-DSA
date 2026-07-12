#Write a program to show the difference between == and is.

lst1=[1,2,3,4]
lst2=[1,2,3,4]
print(lst1==lst2) # == checks the value or both variable is exact same or not.

lst3=lst1
print(lst1 is lst3) # is checks the memory location of both varibales.

lst4=[3,2]
print(lst1 is lst4) # lst1 and last4 both are in different location.

#lst1 and lst2 and lst3 these three variable are shearing same valuse and same memory locations.
