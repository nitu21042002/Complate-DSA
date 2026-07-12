#Write a program to demonstrate logical and and or.

a=10
b=20
print(a and b) #output is 20 because and searches for default and false value 
              # if var1 is true it will check next value 

a=0

print(a and b) #output is 0 because and searches for default and false value 
              # if var1 is false it will print var1 as an output
               
print(a or b) #output is 20 because and searches for non default and true value 
              # if var1 is false it will check next value
a=10

print(a or b) #output is 20 because and searches for non default and true value 
             # if var1 is true it will print var1 as an output