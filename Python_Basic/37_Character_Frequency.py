#Write a program to count the frequency of each character in a string.

st=input("Enter a string : ")
d={}
for i in st:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)