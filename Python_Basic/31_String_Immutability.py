#Write a program to demonstrate string immutability.

st="Nitu Yadav"
print(st)

#st[0]="R" # st[0]="R"
          #  ~~^^^
          #TypeError: 'str' object does not support item assignment due to string immutability

st="R"+st[1::]
print(st) #we can overwrite it but can not modify it
