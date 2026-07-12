#Write a program using the id() function.

a=10
b=10
c=20
print(id(a))
print(id(b)) # a and b id is same because both are pointing same value
print(id(c)) #c id is different because it's value is different
lst=[1,2,3]
lst1=[1,2,3]
print(id(lst)) 
print(id(lst1)) # lst and lst1 have different id both values are same but
                  #they both are stored in different memory location.
lst2=lst
print(id(lst2)) # lst and lst2 both are stored in same memory location having same id.