#Write a program using all() and any().

lst=[1,2,3,4,24]
lst1=[0,1,3,4,2,4]
var=["True","",1,4,2]
var1=["",0,0j,0.0]

#all()  this is check in a collection of values have all the non default values or true value 
# then return true else return false.
print(all(lst))
print(all(lst1))
print(all(var))
print(all(var1))
#any()  this is check in a collection if have any one value is non default or true it will
#  return true else retrun false.
print(any(lst))
print(any(lst1))
print(any(var))
print(any(var1))