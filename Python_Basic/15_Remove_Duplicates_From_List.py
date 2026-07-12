#Write a program to remove duplicate elements from a list.

lst=[1,2,1,3,1,3,31,4,3,2,3,4,2,4,2,1,3,42]
lst=list(set(lst)) #set() 
print(lst)

#using loop
l=[]
for i in lst:
    if i not in l:
        l.append(i)
    
print(l)