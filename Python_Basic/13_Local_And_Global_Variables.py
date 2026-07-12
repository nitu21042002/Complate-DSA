#Write a program to demonstrate local and global variables.

a=10 #global variable
def outer():
    a=20 #local variable
    def inner():
        print("Local variable:",a)
    inner()
print("Global variable :",a)
outer()
