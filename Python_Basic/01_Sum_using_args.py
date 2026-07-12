#Write a program to find the sum of multiple numbers using *args.
def Sum(*args):
    total=0
    for n in args:
        total=total+n
    print(total)

Sum(1,2,3,4,5)