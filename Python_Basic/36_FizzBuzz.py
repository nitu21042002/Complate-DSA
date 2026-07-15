#Write a program to solve the FizzBuzz problem.
#Write a program that prints the numbers from 1 to N.
#For each number:
#If the number is divisible by 3, print "Fizz".
#If the number is divisible by 5, print "Buzz".
#If the number is divisible by both 3 and 5, print "FizzBuzz".
#Otherwise, print the number itself.


num=int(input("Enter a number : "))
for i in range(1,num):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)