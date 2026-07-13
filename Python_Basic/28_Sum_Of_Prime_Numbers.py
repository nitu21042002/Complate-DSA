#Write a program to find the sum of all prime numbers from 1 to N.

n=int(input("Enter a number : "))
def is_prime(n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        else:
            return False

sum=0
for i in range(1,n+1):
    if is_prime(i):
          sum+=i
print("sum of all prime numbers : ",sum)
    

