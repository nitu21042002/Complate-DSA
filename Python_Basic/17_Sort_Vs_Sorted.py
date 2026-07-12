#Write a program to demonstrate the difference between sort() and sorted().

lst=[8,2,4,5,6,1,9]
lst2=[8,5,7,2,9,3,6,4,25,41,85,78]

lst.sort() #sort modify in original lst 
print(lst)

new=sorted(lst2) #sorted does not modify in oringinal list it will creat new list 
print(new) 
print(lst2) #this is unsorted list
print(new is lst2) #sorted list is in new variable 
