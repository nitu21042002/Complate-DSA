#Write a program to print the Fibonacci series.

n=int(input("Enter a number : "))
first_num=0
second_num=1
for i in range(n):
    print(first_num,end=" ")
    first_num,second_num=second_num,first_num+second_num
