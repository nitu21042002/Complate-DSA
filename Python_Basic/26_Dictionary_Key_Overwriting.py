#Write a program to demonstrate dictionary key overwriting (1, 1.0, True).

print(1 == 1.0)    # True
print(1 == True)   # True
print(1.0 == True) # True

d={}
d[1]="integer" 
d[1.0]="float" 
d[True]="boolean" 
print(d)

#(1,1.0,True) all values are internaly equal that's why dictinory take it as same key updated value.