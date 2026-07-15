#Write a program to check whether a string is a palindrome.

st=input("Enter a input : ")
rev=""
for word in st:
    rev=word+rev
if st==rev:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



#Write a program to check whether a number is a palindrome.

num=input("Enter a input : ")
if num == num[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")