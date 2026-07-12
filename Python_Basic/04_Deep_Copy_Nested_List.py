#Write a program to demonstrate deep copy of a nested list.
import copy
lst=[1,2,3,4,[2,3,4,5],9]
lst2=copy.deepcopy(lst) #deepcopy of original list
print(lst2)

lst[2]=19 #modify only original list
print("lst:",lst)

lst[4][2]=10 #modify only original nesedt list
print("lst:",lst)

lst2[2]=20 # modify only copied list
print("lst2:",lst2)

lst2[4][2]=30 # modified only copied nested list 
print("lst2:",lst2)

#deep copy creat entier lst in another memoery location changeing any one list can not modify another one